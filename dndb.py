import psycopg2, sys

"""
Dungeons and Databases, for use with the DnD 4E name generator.
"""
# TO USE A DIFFERENT DATABASE, CHANGE THESE FIELDS
host = 'localhost'
dbname = 'dnd'
user = 'postgres'
password = 'db_pass'

"""
Makes request of given string to database.
"""
def make_request(cur, request):
	try:
		cur.execute(request)
	except:
		print "Selection failed: " + request # let us know where we failed on the select
		sys.exit()

"""
Connect to database with provided credentials and return a cursor connected to it.
"""
def connect_to_names():
	try: # connect to the db
		conn = psycopg2.connect("host=\'" + host + "\' dbname=\'" + dbname + "\' user=\'" + user + "\' password=\'" + password + "\'")
	except:
		print "Unable to connect to the database."	# terminate early if connection fails
		sys.exit()
	return conn.cursor()