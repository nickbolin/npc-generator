import psycopg2, sys, random

"""
Dungeons and Databases, for use with the DnD 4E name generator.
Internalizes all the logic for interacting with the database.
"""
class Database():
	"""
	Connect to database with provided credentials and return a cursor connected to it.
	"""
	def __init__(self):
		# TO USE A DIFFERENT DATABASE, CHANGE THESE FIELDS
		host = 'localhost'
		dbname = 'dnd'
		user = 'postgres'
		password = 'db_pass'

		try: # connect to the db
			self.conn = psycopg2.connect("host=\'" + host + "\' dbname=\'" + dbname + "\' user=\'" + user + "\' password=\'" + password + "\'")
		except:
			print "Unable to connect to the database."	# terminate early if connection fails
			sys.exit()
		self.cur = self.conn.cursor()

	def __del__(self):
		self.conn.close()

	"""
	Makes request of given string to database and returns all results.
	"""
	def make_request(self, request):
		try:
			self.cur.execute(request)
		except:
			print "Selection failed: " + request # let us know where we failed on the select
			sys.exit()

		return self.cur.fetchall()

	"""
	Gets a random name/meaning combo from the database with the given race and type with optional gender.
	Returns values bundled in a dict.
	"""
	def get_name_segment(self, n_type, race, gender=None):
		request = "SELECT name, meaning FROM names WHERE type = \'" + n_type + "\' AND race LIKE \'%" + race + "%\'"

		if gender is not None:
			request += "AND gender=\'" + gender + "\'"
		rows = self.make_request(request)
		
		index = random.randint(0, len(rows) - 1)
		curr_name = (rows[index])[0].strip() # pick a random suffix and trim whitespace
		curr_mean = (rows[index])[1].strip() + " " # get meaning

		return {'name': curr_name, 'meaning': curr_mean}