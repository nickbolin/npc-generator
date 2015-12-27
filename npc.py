import random, sys
import character, dndb, namegen

"""
NPC class and generator for the DnD 4E name generator.
"""

# Alignments for characters
alignments = ['Lawful Good', 'Lawful Evil', 'Lawful Neutral', 'Chaotic Neutral', 'Chaotic Evil', 'Chaotic Good', 'Good', 'Evil', 'True Neutral']

"""
NPC class for generation. Extends functionality of Character class with added notes for NPCs.
"""	
class NonPC(character.Character):
	def __init__(self):
		self.gen = namegen.NameGenerator()

		super(NonPC, self).__init__() # call Character initializer
		self.commoner = None	# boolean to determine if character is an adventurer or commoner
		self.alighment = None 	# lawful, evil, good, neutral, etc
		
	"""
	Creates an NPC on a few criteria
	commoner = boolean for commoner status
	gender = male/female etc.
	race = Elf, Halfling, etc.
	level = selbstverstandlich
	meaning = name meaning (this is generated by the method, as is the name)
	"""
	def generate_npc(self, commoner=None, gender=None, race=None, level=None, profession=None):
		# generate basic demographics as needed
		if commoner is None:
			self.commoner = random.choice([True, False]) # random, if needed
		else: 
			self.commoner = commoner
		
		if profession is None: # set the character's class, if needed
			# pick a class, but consider an adventurer vs townsperson setting
			self.profession = random.choice(character.com_classes if self.commoner else character.adv_classes)
		else:
			self.profession = profession # TODO, consider checking to ensure only allowed classes are created

		if race is None:
			self.race = random.choice(character.races) # gen race, if needed
		else:
			self.race = race
		
		if level is None:
			self.level = random.randint(1, 30) # gen level between 1 and 30
		else:
			self.level = int(level) % 30 # cap level at 30

		if gender is None:
			self.gender = random.randint(0, 1) # generate gender 0 = Male, 1 = Female
		else:
			self.gender = character.genders[gender]

		# generate name based on gender and race
		name_dict = self.gen.gen_name(self.gender, self.race) 

		self.name = name_dict['name']
		self.meaning = name_dict['meaning']

		# generate alighment
		self.alignment = random.choice(alignments)

		# do stats to level
		scores = [16, 14, 13, 12, 11, 10] # default Player's Handbook way to determine ability scores
		for key in self.stats:
			random.shuffle(scores)
			self.stats[key] = scores.pop()
		# then add race/level calculations
		self.add_racial_stat_bonus()
		self.add_level_stat_bonus()

		# consider physical description/personality selections
		#	place of origin
		#	organizations
		#	motivations
		#	background

	"""
	Stringify our character in a nice way
	"""
	def __str__(self):
		# print name and basic race, level, class info
		result = self.name + " is a level " + str(self.level) + " " + self.race + " " + self.profession + ".\n"
		# alignment and name meaning (these fields are not included in Character)
		pronoun = 'He' if self.gender == 0 else 'She'
		result += pronoun + " is considered " + self.alignment + ".\n"
		pos_pronoun = 'His' if self.gender == 0 else 'Her'
		result += pos_pronoun + " name means " + self.meaning + ".\n"
		# add stats
		result += "STR: " + str(self.stats['STR']) + " CON: " + str(self.stats['CON']) + " DEX: " + str(self.stats['DEX']) + " INT: " + str(self.stats['INT']) + " WIS: " + str(self.stats['WIS']) + " CHA: " + str(self.stats['CHA']) + ". "
		# insert remainder of demographics (personality, physical appearance, etc)
		return result