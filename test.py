#!/usr/local/bin/python
import argparse, sys
import npc

"""
Run a single test with given parameters
"""
def run_test(gender=None, race=None, commoner=None, level=None, profession=None):
	header = "Generating a random "	# always start the same way
	if gender is not None:		# print gender, if provided
		header += gender + " "
	if level is not None:		# include level if provided
		header += "level " + str(level) + " "
	if race is not None:		# specify race if provided
		header += race + " "
	header += "NPC with " 		# always include this
	if commoner is not None:
		header += ('commoner' if commoner else 'adventurer') + " "
	else:
		header += "default "
	header += "settings:"
	print header
	current_npc = npc.NonPC()

	current_npc.generate_npc(commoner=commoner, race=race, gender=gender, level=level, profession=profession)

	print current_npc
	print

"""
A suite of simple tests to ensure that all basic functionality works.
"""
def run_basic_test():
	print "Running basic tests:"
	run_test()
	run_test(race='Half-elf')
	run_test(gender='Female')
	run_test(commoner=False)
	run_test(level=21)
	run_test(race='Dwarf', gender='Male', commoner=False, level=29)

def run_race_test(race):
	print "Running a race test on " + race + ":"
	run_test(race=race, gender='Male')
	run_test(race=race, gender='Female')
	run_test(race=race, commoner=False)
	run_test(race=race, commoner=True)
	run_test(race=race, level=1)
	run_test(race=race, level=15)
	run_test(race=race, level=30)
	run_test(race=race, gender='Male', commoner=False, level=27)
	run_test(race=race, gender='Female', commoner=True, level=23)		

"""
Main
"""
parser = argparse.ArgumentParser(description='A test driver for npc.py')
# add arguments for npc customization
parser.add_argument('-r', '--race', help='specify the race of the npc to generate')
parser.add_argument('-g', '--gender', help='specify the gender of the npc to generate (Male/Female)')
parser.add_argument('-l', '--level', help='specify the level of the npc to generate', type=int)
parser.add_argument('-c','--commoner', help='specify that the npc is a commoner', action='store_true')
parser.add_argument('-a', '--adventurer', help='specify that the npc is an adventurer', action='store_true')
parser.add_argument('-p', '--profession', help='specify the class of the npc')
# add some utility arguments
parser.add_argument('--count', help='number of characters to generate with these settings', type=int)
parser.add_argument('--basic', help='run a basic series of tests', action='store_true')
parser.add_argument('--race_test', help='run a series of standard tests on a single race')

args = parser.parse_args()
if args.count:				# get the number of loops, set default to 1
	count = args.count
else:
	count = 1

if args.basic:				# run a basic test as many times as count dictates
	for x in range(count):
		run_basic_test()
	sys.exit()

if args.race_test:			# run a test of all functionality on a specific race
	for x in range(count):
		run_race_test(args.race_test)
	sys.exit()

# otherwise, run a regular test with appropriate fields

if args.race:				# set the race, default to None
	npc_race = args.race
else:
	npc_race = None

if args.gender:				# set the gender, default to None
	npc_sex = args.gender
else:
	npc_sex = None

if args.level:				# set the level, default to None
	npc_level = args.level
else:
	npc_level = None

if args.commoner:			# set the commoner attribute, default to None
	npc_common = True
elif args.adventurer:
	npc_common = False
else:
	npc_common = None

if args.profession:			# set the class of the character, default to None
	npc_profession = args.profession
else:
	npc_profession = None

# run the appropriate number of tests
for x in range(count):
	run_test(gender=npc_sex, race=npc_race, level=npc_level, commoner=npc_common, profession=npc_profession)