import time
from boto.dynamodb2.table import Table
import boto.dynamodb2.exceptions
import psycopg2

# AWS constants
REGION = 'eu-west-1'

# PSQL CONN PARAMETERS
DB_HOST = 'HOST.rds.amazonaws.com'
DB_USER = 'USER'
DB_PASS = 'PWD'
DB_NAME = 'smartgrid'
CONN_STRING = "dbname=%s user=%s host=%s password=%s" % (DB_NAME, DB_USER, DB_HOST, DB_PASS)

QUERY_DELAY = 10
QLIMIT = 10
ZONE_IDS = ('E','B','L')


def tprint(string):
	now = time.ctime()
	print(now + '\t ' + str(string))

if __name__ == '__main__':
	ddb = boto.dynamodb2.connect_to_region(REGION)
	tprint(str(ddb))
	conn = psycopg2.connect(CONN_STRING)


	while True:
		for z in ZONE_IDS:
			
			table_name = 'sg_%s_21' % z
			tprint("Processing table %s" % table_name)
			table = Table(table_name, connection=ddb)
			now = time.time()

			try:
				res = table.query_2(
					is_etl_processed__eq=0,
					etl_ts__lte=now,
					index='ETLIndex',
					limit=QLIMIT
				)
			except Exception, err:
				print Exception, err

			else:
				tprint('processing...')
				for r in res:
					print "DDB ok",
					if r['elaboration_ts'] is None:
						r['elaboration_ts'] = time.time()
					if r['measurement_ts'] is None:
						r['measurement_ts'] = time.time()
					if r['processing_ts'] is None:
						r['processing_ts'] = time.time()
					if r['receive_ts'] is None:
						r['receive_ts'] = time.time()
					if r['send_ts'] is None:
						r['send_ts'] = time.time()

					with conn, conn.cursor() as cur:
						cur.execute(
				            """
							INSERT INTO sg_21 
							(
							    zone_id, sender_id, etl_ts, elaboration_ts, measurement_ts, processing_ts, receive_ts, send_ts, 
							    fattore_potenza, frequenza_rete, corrente_fase, tensione_fase, energia_attiva_immisione, 
							    energia_attiva_prelievo, energia_reattiva_immissione, energia_reattiva_prelievo, potenza_apparente, 
							    potenza_attiva, potenza_reattiva
							) 
							VALUES 
							(
							    %s,%s,now(),to_timestamp(%s),to_timestamp(%s),to_timestamp(%s),to_timestamp(%s),
							    to_timestamp(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
							 )
							""" , 
							(
							     	z,r['sender_id'],r['elaboration_ts'],r['measurement_ts'],r['processing_ts'],
							     	r['receive_ts'],r['send_ts'],r['fattore_potenza'], r['frequenza_rete'], r['corrente_fase'], 
							     	r['tensione_fase'], r['energia_attiva_immisione'], r['energia_attiva_prelievo'], 
							     	r['energia_reattiva_immissione'], r['energia_reattiva_prelievo'], r['potenza_apparente'], 
							     	r['potenza_attiva'], r['potenza_reattiva']
							)
						)
										
						r['is_etl_processed'] = 1
						r.save(overwrite=True)
						print "PG ok",

		tprint('sleeping for %d seconds' % QUERY_DELAY)
		time.sleep(QUERY_DELAY)
		tprint('waking up')
		continue
	cur.close()
	conn.close()

