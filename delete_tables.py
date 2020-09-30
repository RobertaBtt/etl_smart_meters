import boto.dynamodb2

# AWS constants
REGION = 'eu-west-1'
EXC = (
	'sg_B_21',
	'sg_E_21',
	'sg_E_30',
	'sg_L_21',
	'sg_msg_log'
)

if __name__ == '__main__':
	ddb = boto.dynamodb2.connect_to_region(REGION)
	tables_list = ddb.list_tables()['TableNames']

	print ("starting deletion...")

	deleted = 0
	skipped = 0

	for table_name in tables_list:
		if table_name in EXC:
			skipped += 1
			print "skipping %s" % table_name
		else:
			try:
				ddb.delete_table(table_name)
			except:
				pass
			else:
				print "deleted %s" % table_name
				deleted += 1
			

	print "%d tables deleted (%d skipped)" % (deleted, skipped)


