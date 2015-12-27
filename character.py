import random

# Character races
races = ['Orc', 'Human', 'Elf', 'Half-elf', 'Half-orc', 'Dwarf', 'Tiefling', 'Gnome', 'Eladrin', 'Dragonborn', 'Halfling']

# Languages that are known in the realm
languages = ['Common', 'Deep Speech', 'Draconic', 'Dwarven', 'Elven', 'Giant', 'Goblin', 'Primordial', 'Supernal', 'Abyssal']

# Adventurer classes
adv_classes = ['Cleric', 'Fighter', 'Paladin', 'Ranger', 'Rogue', 'Warlock', 'Warlord', 'Wizard']

# Commoner classes
com_classes = ['Bartender', 'Slave', 'Merchant', 'Farmer', 'Guard', 'Nobleman', 'Priest', 'Craftsman', 'Miner', 'Blacksmith', 'Bard']

# Genders as needed
genders = {'Male': 0, 'Female': 1}

# lookup table for stats
stat_lookup = {0: 'STR', 1: 'CON', 2: 'DEX', 3: 'INT', 4: 'WIS', 5: 'CHA'}

"""
Skeleton class for a character
"""
class Character(object):
	def __init__(self):
		self.name = None 		# selbstverstandlich
		self.meaning = None 	# meaning of the name
		self.level = None 		# used in defining appropriate stats and influence
		self.gender = None		# M/F or None at all
		self.race = None		# right now, just PC races
		# Strength, Constitution, Dexterity, Intelligence, Wisdom, Charisma
		self.stats = {'STR': 0, 'CON': 0, 'DEX': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}
		self.profession = None	# class

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
		elif self.race == 'Gnome':
			self.stats['INT'] += 2
			self.stats['CHA'] += 2
		elif self.race == 'Half-elf':
			self.stats['CON'] += 2
			self.stats['CHA'] += 2
		elif self.race == 'Halfling':
			self.stats['DEX'] += 2
			self.stats['CHA'] += 2
		elif self.race == 'Human':
			self.stats['STR'] += 2
		elif self.race == 'Orc':
			self.stats['STR'] += 2
			self.stats['CON'] += 2
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
			self.stats[stat_lookup[index]] += 1 # TODO: make this not random?
