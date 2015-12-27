import dndb
import random

"""
Name generator that queries our database with various parameters to construct a random name.
"""
class NameGenerator():

	def __init__(self):
		self.db = dndb.Database()
	"""
	Generates a name for our character.
	Like all race-specific name generator methods, this returns a dict structure with 'name' and 'meaning' fields.
	"""
	def gen_name(self, gender, race):
		gend = 'male' if gender == 0 else 'female'

		if race == 'Half-elf':					# check multirace cases
			races = "Elf%\' OR race LIKE \'%" + "Human"
		elif race == 'Half-orc':
			races = "Orc%\' OR race LIKE \'%" + "Human"
		elif race == 'Dwarf':					# or non-conventional names
			return self.dwarf_name(gend)			# dwarves have two part first names and clan names
		elif race == 'Elf':
			return self.elf_name(gend)				# elves have a ton of name combinations
		elif race == 'Gnome':
			return self.gnome_name(gend)			# gnomes have 1-3 part names
		else:
			races = race

		request = "SELECT name, meaning FROM names WHERE gender = \'" + gend + "\' AND race LIKE \'%" + races + "%\'"
		rows = self.db.make_request(request)
		
		return random.choice(rows) if rows else {'name': 'No name', 'meaning': 'pregnant whale'}

	"""
	Creates a dwarven name in standard dwarven custom. There are neuter prefixes, and gender determines the suffix.
	Returns a dict with 'name' and 'meaning' as their respective values.
	"""
	def dwarf_name(self, gender):
		name_dict = self.db.get_name_segment(race='Dwarf', n_type='prefix')
		curr_name += name_dict['name']
		curr_mean += name_dict['meaning']

		name_dict = self.db.get_name_segment(race='Dwarf', n_type='suffix', gender=gender)
		curr_name += name_dict['name'] # pick a random suffix and trim whitespace
		curr_mean += name_dict['meaning'] # get meaning

		return {'name': curr_name, 'meaning': curr_mean.strip()}

	"""
	Creates a first name in gnomish custom. 
	"""
	def gnome_name(self, gender):
		nicknamed = False
		roll = random.randint(1, 10) # d10 roll
		if roll <= 4:
			count = 1	# 1-4 gets short name
		elif roll <= 7:	# 5-7 gets regular name
			count = 2
		elif roll <= 9:
			nicknamed = True
			count = 2	# 8-9 gets a nickname with their name
		elif roll == 10:	# 10 gets long name
			count = 3

		curr_name = ""
		curr_mean = ""

		for x in range(0, count):
			name_dict = self.db.get_name_segment(race='Gnome', n_type='fragment')
			curr_name += name_dict['name']
			curr_mean += name_dict['meaning']
		
		curr_name = curr_name.capitalize() + " "

		if nicknamed:
			name_dict = self.db.get_name_segment(race='Gnome', n_type='suffix')
			curr_name += "\"" + name_dict['name'] + "\""
			# curr_mean += name_dict['mean'] # get meaning for the nickname (if we want to?)
		else:
			curr_mean = curr_mean.strip()
			curr_name = curr_name.strip() # eliminate trailing spaces

		return {'name': curr_name, 'meaning': curr_mean}

	"""
	Creates a first name for an elf. 
	"""
	def elf_name(self, gender):
		roll = random.randint(1, 10)
		if roll <= 4:	# 0-4 is a prefix + suffix (Er + avel)
			name_dict = self.db.get_name_segment(race='Elf', n_type='prefix')
			curr_name = name_dict['name']
			curr_mean = name_dict['meaning']

			name_dict = self.db.get_name_segment(race='Elf', n_type='suffix', gender=gender)
			curr_name += name_dict['name'] # pick a random suffix and trim whitespace
			curr_mean += name_dict['meaning'] # get meaning
		elif roll <= 7:	# 4-7 is prefix + 2 suffices (Von + an + or)
			name_dict = self.db.get_name_segment(race='Elf', n_type='prefix')
			curr_name = name_dict['name']
			curr_mean = name_dict['meaning']

			for x in range(2):
				name_dict = self.db.get_name_segment(race='Elf', n_type='suffix', gender=gender)
				curr_name += name_dict['name'] # pick a random suffix and trim whitespace
				curr_mean += name_dict['meaning'] # get meaning
		elif roll <= 9:	# 7-9 is prefix + suffix then prefix + suffix for two names (Lam + en Tho + sar)
			curr_name = ""
			curr_mean = ""
			for x in range(2):
				name_dict = self.db.get_name_segment(race='Elf', n_type='prefix')
				curr_name += name_dict['name']
				curr_mean += name_dict['meaning']

				name_dict = self.db.get_name_segment(race='Elf', n_type='suffix', gender=gender)
				curr_name += name_dict['name'] # pick a random suffix and trim whitespace
				curr_mean += name_dict['meaning'] # get meaning

				curr_name += " "
		else:	# 10 is suffix + apostrophe + prefix + 2 suffices (Que + ' + ael + ti + wyn)
			name_dict = self.db.get_name_segment(race='Elf', n_type='suffix', gender=gender)
			curr_name = name_dict['name'] # pick a random suffix and trim whitespace
			curr_mean = name_dict['meaning'] # get meaning



			curr_name = curr_name.strip()
			curr_mean = curr_mean.strip()

		return {'name': curr_name, 'meaning': curr_mean}
