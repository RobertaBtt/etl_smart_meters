import struct
import time
from boto.dynamodb2.table import Table
import boto.dynamodb2.exceptions
import base64
import sys

ALLOWED_MSG_CLASS_IDS = ('E', 'A', 'T')

if len(sys.argv) > 1 and sys.argv[-1] in ALLOWED_MSG_CLASS_IDS:
	MSG_CLASS_ID = sys.argv[-1]
else:
	MSG_CLASS_ID = 'E'

# AWS constants
REGION = 'eu-west-1'

# Protocol constants
ENDIANESS = '>'
HEADER_FMT = 'B2dBHb'
HEADER_LEN = struct.calcsize(ENDIANESS + HEADER_FMT)
HEADER_PADDING = '%dx' % HEADER_LEN
HEADER_FIELDS = (
	'API_version',
	'measurement_ts',
	'send_ts',
	'msg_id',
	'content_length',
	'CRC'
)

from messages import MESSAGES

QUEUE_PREFIX = 'sg_msg_'
POLL_DELAY = 10 #seconds to wait when the queue is empty

def tprint(string):
	now = time.ctime()
	print(now+'\t '+ str(string))

if __name__ == '__main__':
	ddb = boto.dynamodb2.connect_to_region(REGION)
	tprint(str(ddb))
	sqs = boto.sqs.connect_to_region(REGION)
	tprint(str(sqs))
	queue_name = QUEUE_PREFIX + MSG_CLASS_ID
	queue = sqs.get_queue(queue_name)

	print queue_name
	print queue
	print queue.count()

	while True:
		m = queue.read(message_attributes=['topic', 'receive_ts', 'payload_hash'])

		if m is None:
			tprint('queue is empty: sleeping for %d seconds' % POLL_DELAY)
			time.sleep(POLL_DELAY)
			tprint('waking up')
			continue

		item = {}

		payload_hash = item['payload_hash'] = m.message_attributes['payload_hash']['string_value']
		topic = item['topic'] = m.message_attributes['topic']['string_value']
		item['receive_ts'] = float(m.message_attributes['receive_ts']['string_value'])

		zone_id, profile_id, sender_id, recipient_id, msg_class_id = topic.split('/')

		item['sender_id'] = sender_id

		payload = base64.decodestring(m.get_body())


		logs = Table('sg_msg_log', connection=ddb)
		log_items = logs.query_2(
			payload_hash__eq = payload_hash,
			limit = 1
		)

		header = payload[:HEADER_LEN]
		header_fields = struct.unpack(ENDIANESS + HEADER_FMT, header)

		for i, field_name in enumerate(HEADER_FIELDS):
			item[field_name] = header_fields[i]

		try:
			msg_name, msg_fmt, msg_fields = MESSAGES[header_fields[3]]
		except KeyError:
			tprint('message read with an unknown MSG-ID (%d)' % header_fields[3] )
			for log_item in log_items:
				log_item['err'] = 'ERR_UNKNOWN_MSG_ID_%d' % header_fields[3]
				log_item.partial_save()
				queue.delete_message(m)
		else:
			if not msg_fmt:
				tprint('MSG_ID (%d) has an empty message format' % header_fields[3])
				queue.delete_message(m)
				continue
		
			tprint('message read (%s on %s)' % (msg_name, zone_id) )

			try:
				fields = struct.unpack(ENDIANESS + msg_fmt, payload[HEADER_LEN:])
			except Exception, err:
				print "MSG_ID (%d) generated %s - was %d bytes long, *NOT* removed from queue" % (
					header_fields[3],
					err,
					struct.calcsize(ENDIANESS + msg_fmt)
				)
				continue
				
			for i, field_name in enumerate(msg_fields):
				item[field_name] = fields[i]

			item['elaboration_ts'] = time.time()
			# let's add fields for ETL processing
			item['is_etl_processed'] = 0
			item['etl_ts'] = 0

			table_name = 'sg_%s_%d' % (zone_id, header_fields[3])
			table = Table(table_name, connection=ddb)

			try:
				old_item = table.get_item(payload_hash=payload_hash)
			except boto.dynamodb2.exceptions.ItemNotFound:
				print payload_hash
				table.put_item(item)
				print "saved on dynamodb"
			else:
				print payload_hash
				print '===> ', list(old_item)
				print '===>', item.values()
				queue.delete_message(m)
				tprint('found duplicated message: deleted it from SQS')
			finally:
				queue.delete_message(m)
