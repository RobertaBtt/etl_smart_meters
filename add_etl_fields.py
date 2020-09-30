import time
from boto.dynamodb2.table import Table
import boto.dynamodb2.exceptions

"""
adds ETL fields (is_etl_processed and etl_ts) to legacy rows
"""


# AWS constants
REGION = 'eu-west-1'


DELAY = 10
QLIMIT = 10
ZONE_IDS = ('E' ,'B','L')


def tprint(string):
	now = time.ctime()
	print(now + '\t ' + str(string))

if __name__ == '__main__':
	ddb = boto.dynamodb2.connect_to_region(REGION)
	tprint(str(ddb))

	while True:
		for zone_id in ZONE_IDS:
			tprint('processing zone_id %s' % zone_id)

			table_name = 'sg_%s_21' % zone_id
			tprint("Processing table %s" % table_name)

			table = Table(table_name, connection=ddb)
			res = table.scan(
				is_etl_processed__null = None,
			)

			saved = 0
			for item in res:
				try:
					item['is_etl_processed'] = 0
					item['etl_ts'] = 0
					item.save()
					saved += 1

					print ".",
				except boto.dynamodb2.exceptions.ProvisionedThroughputExceededException:
					print "ProvisionedThroughputExceededException: sleeping %d secs" % DELAY
					print "%d saved so far" % saved
					time.sleep(DELAY)
					print "Waking up..."
					continue
				except Exception, err:
					print err
					print "Unknown error, going on"
					continue
			else:
				print "%d updated" % saved
