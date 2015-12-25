import random, sys
import character
import psycopg2

# Alignments for characters
alignments = ['Lawful Good', 'Lawful Evil', 'Lawful Neutral', 'Chaotic Neutral', 'Chaotic Evil', 'Chaotic Good', 'Good', 'Evil', 'True Neutral']

def gen_name(gender, race):
	try: # connect to the db
		conn = psycopg2.connect("host='localhost' dbname='dnd' user='postgres' password='db_pass'")
	except:
		print "Unable to connect to the database."	# terminate early if connection fails
		sys.exit()

	cur = conn.cursor() # get cursor for requests

	gend = 'male' if gender == 0 else 'female'

	if race == 'Half-elf':
		races = "Elf%\' OR \'%" + "Human"
	elif race == 'Half-orc':
		races = "Orc%\' OR \'%" + "Human"
	else:
		races = race

	request = "SELECT name FROM names WHERE gender = \'" + gend + "\' AND race LIKE \'%" + races + "%\'"

	try:
		cur.execute(request)
	except:
		print "Selection failed"
		sys.exit()

	rows = cur.fetchall()

	return random.choice(rows)[0].strip() if rows else 'No name'


"""
NPC class for generation. Can eventually should be adapted for PCs
"""	
class NonPC(character.Character):
	def __init__(self):
		super(NonPC, self).__init__() # call Character initializer
		self.commoner = None	# boolean to determine if character is an adventurer or commoner
		self.alighment = None 	# lawful, evil, good, neutral, etc
		

	"""
	Creates an NPC on a few criteria
	commoner = boolean for commoner status
	gender = male/female etc.
	race = Elf, Halfling, etc.
	level = selbstverstandlich
	"""
	def generate_npc(self, commoner=None, gender=None, race=None, level=None):
		# generate basic demographics as needed
		if commoner == None:
			self.commoner = random.choice([True, False]) # random, if needed
		else: 
			self.commoner = commoner
		if race == None:
			self.race = random.choice(character.races) # gen race, if needed
		else:
			self.race = race
		if level == None:
			self.level = random.randint(1, 30) # gen level between 1 and 30
		else:
			self.level = level
		if gender == None:
			self.gender = random.randint(0, 1) # generate gender 0 = Male, 1 = Female
		else:
			self.gender = character.genders[gender]

		# generate name based on gender and race
		self.name = gen_name(self.gender, self.race) 

		# generate alighment
		self.alignment = random.choice(alignments)

		# pick a class, but consider an adventurer vs townsperson setting
		self.profession = random.choice(character.com_classes if self.commoner else character.adv_classes)

		# do stats to level
		scores = [16, 14, 13, 12, 11, 10] # default Player's Handbook way to determine ability scores
		for key in self.stats:
			random.shuffle(scores)
			self.stats[key] = scores.pop()
		# then add race/level calculations
		self.add_racial_stat_bonus()
		self.add_level_stat_bonus()

		# consider physical description/personality

	"""Adds stat bonuses depending on races."""
	def add_racial_stat_bonus(self):
		if self.race == 'Dragonborn':
			self.stats['STR'] += 2
			self.stats['CHA'] += 2
		elif self.race == 'Dwarf':
			self.stats['CON'] += 2
			self.stats['WIS'] += 2
		elif self.race == 'Eladrin':
			self.stats['DEX'] += 2
			self.stats['INT'] += 2
		elif self.race == 'Elf':
			self.stats['DEX'] += 2
			self.stats['WIS'] += 2
		elif self.race == 'Half-elf':
			self.stats['CON'] += 2
			self.stats['CHA'] += 2
		elif self.race == 'Halfling':
			self.stats['DEX'] += 2
			self.stats['CHA'] += 2
		elif self.race == 'Human':
			self.stats['STR'] += 2
		elif self.race == 'Tiefling': # TODO: add other PC races
			self.stats['INT'] += 2
			self.stats['CHA'] += 2

	"""Adds stat bonuses depending on current character level."""
	def add_level_stat_bonus(self):
		points = 0
		if self.level >= 28: 	# determine number of points to distribute
			points += 12
		elif self.level >= 24:
			points += 10
		elif self.level >= 18:
			points += 8
		elif self.level >= 14:
			points += 6
		elif self.level >= 8:
			points += 4
		elif self.level >= 4:
			points += 2

		if self.level >= 21:	# at each of level 21 and 11 increase each score by 1
			for key in self.stats:
				self.stats[key] += 2
		elif self.level >= 11:
			for key in self.stats:
				self.stats[key] += 1

		for x in range(points):	# distribute the points
			index = random.randint(0, 5)
			self.stats[character.stat_lookup[index]] += 1 # TODO: make this not random?


	"""Stringify our character in a nice way"""
	def __str__(self):
		# print name and basic race, level, class info
		result = self.name + " is a level " + str(self.level) + " " + self.race + " " + self.profession + ".\n"
		# alignment 
		pronoun = 'He' if self.gender == 0 else 'She'
		result += pronoun + " is considered " + self.alignment + ".\n"
		# add stats
		result += "STR: " + str(self.stats['STR']) + " CON: " + str(self.stats['CON']) + " DEX: " + str(self.stats['DEX']) + " INT: " + str(self.stats['INT']) + " WIS: " + str(self.stats['WIS']) + " CHA: " + str(self.stats['CHA']) + ". "
		# insert remainder of demographics (personality, physical appearance, etc)
		return result