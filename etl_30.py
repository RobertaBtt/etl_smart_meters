import time
from boto.dynamodb2.table import Table
import boto.dynamodb2.exceptions
import psycopg2
from decimal import Decimal

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
			
			table_name = 'sg_%s_30' % z
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
							INSERT INTO sg_30 
							(
								zone_id, sender_id, etl_ts, elaboration_ts, measurement_ts, processing_ts, receive_ts, send_ts, API_version,
								alta_tensione, alta_tensione_base10min, bassa_tensione, basso_fattore_potenza, contatore_non_riconosciuto,
								corruzione_registri_energia, intervento_limitatore, inversione_fasi, manomissione, no_power, overflow_tensione,
								problemi_rete_2g3g, sotto_frequenza_rete, sovra_frequenza_rete, sovra_o_sotto_tensione, supero_pmax_perc,
								supero_pmax_contr_perc, supero_traffico_sim1, supero_traffico_sim2, switch_user_leds, usb_removed 
							) 
							VALUES 
							(
								%s,%s,now(),to_timestamp(%s),to_timestamp(%s),to_timestamp(%s),to_timestamp(%s),
								to_timestamp(%s), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
								%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
							 )
							""" , 
							[ 
								
										z,r['sender_id'],r['elaboration_ts'],r['measurement_ts'],r['processing_ts'],
										r['receive_ts'],r['send_ts'], r['API_version']
							] +
							[
								bool(x) if isinstance(x,Decimal) else x for x in 
								(
										
										r['alta_tensione'], r['alta_tensione_base10min'],
										r['bassa_tensione'], r['basso_fattore_potenza'], r['contatore_non_riconosciuto'],
										r['corruzione_registri_energia'], r['intervento_limitatore'], r['inversione_fasi'], r['manomissione'],
										r['no_power'], r['overflow_tensione'], r['problemi_rete_2g3g'], r['sotto_frequenza_rete'], r['sovra_frequenza_rete'],
										r['sovra_o_sotto_tensione'], r['supero_pmax_%'], r['supero_pmax_contr_%'], r['supero_traffico_sim1'],
										r['supero_traffico_sim2'], r['switch_user_leds'], r['usb_removed'] 
								)

							]
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

