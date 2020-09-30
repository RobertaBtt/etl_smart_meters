import boto.dynamodb2
from boto.dynamodb2.table import Table
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
import messages
# AWS constants
REGION = 'eu-west-1'
ZONE_IDS = (
	'E', 
	'L', 
	'B'
)


ETL_MSG_IDS = (
    21,
    30
)

MSG_IDS = messages.MESSAGES.keys()

if __name__ == '__main__':
	ddb = boto.dynamodb2.connect_to_region(REGION)
	tables_list = ddb.list_tables()['TableNames']

	print("starting creation...")

	created = 0
	skipped = 0
	for zone_id in ZONE_IDS:
		for msg_id in MSG_IDS:
			table_name = 'sg_%s_%s' % (zone_id, msg_id)
			if table_name in tables_list:
				skipped += 1
			else:
				kwargs = {
					'schema': [HashKey('payload_hash')],
					'connection': ddb,
					'throughput' : {
						'read': 2,
						'write': 2
					}
				}
			
				if msg_id in ETL_MSG_IDS:
					kwargs['global_indexes'] = [
						GlobalAllIndex(
							'ETLIndex',
							parts = [
								HashKey('is_etl_processed'),
								RangeKey('etl_ts')
							],
							throughput = {
								'read': 2,
								'write': 2
							}
						)
					]
					
				index_message = "with ETLIndex" if 'global_indexes' in kwargs else ""
				table = Table.create(table_name, **kwargs)
				print("created %s (%s) %s" % (table_name, table, index_message))
				created += 1

	print("%d tables created (%d skipped)" % (created, skipped))


