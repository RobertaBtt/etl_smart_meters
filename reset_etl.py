import time
from boto.dynamodb2.table import Table
import boto.dynamodb2.exceptions

# AWS constants
REGION = 'eu-west-1'

# PSQL CONN PARAMETERS
DB_HOST = 'HOST.rds.amazonaws.com'
DB_USER = 'USER'
DB_PASS = 'PWD'
DB_NAME = 'smartgrid'

POLL_DELAY = 10
QLIMIT = 10
ZONE_IDS = ('E',) #,'B','L')


def tprint(string):
	now = time.ctime()
	print(now + '\t ' + str(string))

if __name__ == '__main__':
	ddb = boto.dynamodb2.connect_to_region(REGION)
	tprint(str(ddb))

	table_name = 'sg_E_21'
	tprint("Processing table %s" % table_name)
	table = Table(table_name, connection=ddb)
	res = table.query_2(
		is_etl_processed__eq=1,
		index='ETLIndex',
	)
	
	saved = 0
	for item in res:
		print ".",
		item['is_etl_processed'] = 0
		item.save()
		saved += 1
	else:
		print "%d updated" % saved
