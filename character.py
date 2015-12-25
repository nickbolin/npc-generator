
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
		self.level = None 		# used in defining appropriate stats and influence
		self.gender = None		# M/F or None at all
		self.race = None		# right now, just PC races
		# Strength, Constitution, Dexterity, Intelligence, Wisdom, Charisma
		self.stats = {'STR': 0, 'CON': 0, 'DEX': 0, 'INT': 0, 'WIS': 0, 'CHA': 0}
		self.profession = None	# class