import paho.mqtt.client as mqtt
import time
from hashlib import md5
import os.path
import boto.sqs
from boto.dynamodb2.table import Table
from boto.dynamodb.types import Binary
from boto.sqs.message import Message
import sys

if len(sys.argv) > 1:
	TOPIC = sys.argv[-1]
else:
	TOPIC = '#'


# AWS constants
REGION = 'eu-west-1'

# MQTT constants
USE_SSL = True
CA_CERTS = os.path.join(os.path.curdir, 'ca.crt')
CERTFILE = os.path.join(os.path.curdir, 'client.crt')
KEYFILE = os.path.join(os.path.curdir, 'client.key')

def tprint(string):
	now = time.ctime()
	print(time.ctime() +'\t '+string)

BROKER = 'etl.company.org'

ddb = boto.dynamodb2.connect_to_region(REGION)
tprint(str(ddb))
sqs = boto.sqs.connect_to_region(REGION)
tprint(str(sqs))

def on_connect(client, userdata, flags, rc):
	using_ssl = "" if not USE_SSL else "(using SSL)"
	tprint("Connected to %s %s with result code %s" % (BROKER, using_ssl, str(rc)))
	client.subscribe(TOPIC)
	tprint("Subscribed to %s" % TOPIC)

# The callback for when a PUBLISH message is received from the broker.
def on_message(client, userdata, msg):
	tprint(msg.topic)
	receive_time = time.time()
	digest = md5(msg.payload).hexdigest()

	# SQS setup stuff: we'll do it now to check if queue exists
	queue_prefix = 'sg_msg_'
	msg_class_id = msg.topic.split('/')[-1] #TODO: check topic consistency
	queue_name = queue_prefix + msg_class_id
	queue = sqs.get_queue(queue_name)

	item = {
		'receive_ts': receive_time,
		'payload_hash': digest,
		'payload': Binary(msg.payload),
		'topic': msg.topic
	}

	if queue is None:
		item['err'] = 'ERR_INVALID_TOPIC'
		tprint('invalid topic: %s' % msg.topic)

	log_table = Table('sg_msg_log', connection=ddb)
	log_table.put_item(item)

	tprint("saved on dynamodb %s" % digest)

	if queue is not None:
		m = Message()
		m.message_attributes = {
			'topic': {
						'data_type': 'String',
						'string_value': msg.topic
			},

			'receive_ts': {
						'data_type': 'Number',
						'string_value': str(receive_time)
			},

			'payload_hash' : {
						'data_type': 'String',
						'string_value': digest
			}
		}
		m.set_body(msg.payload)
		queue.write(m)
		tprint("saved to SQS.")


if __name__ == '__main__':
	client = mqtt.Client()

	if USE_SSL:
		client.tls_set(CA_CERTS, CERTFILE, KEYFILE)

	client.on_connect = on_connect
	client.on_message = on_message

	client.connect(BROKER, 8883, 60)
	client.loop_forever()
