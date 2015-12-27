#!/usr/local/bin/python
import npc

print "Generating a random NPC with complete default settings:"
mynpc = npc.NonPC()
mynpc.generate_npc()
print mynpc 
print

print "Generating a random Elf NPC with adventurer settings:"
elfadv = npc.NonPC()
elfadv.generate_npc(commoner=False, race='Elf')
print elfadv 
print

print "Generating a random Dwarf NPC with adventurer settings:"
dwarfadv = npc.NonPC()
dwarfadv.generate_npc(commoner=False, race='Dwarf')
print dwarfadv 
print

print "Generating a random Gnome NPC with adventurer settings:"
gnomeadv = npc.NonPC()
gnomeadv.generate_npc(commoner=False, race='Gnome')
print gnomeadv 
print

print "Generating a male random NPC with commoner settings:"
malecom = npc.NonPC()
malecom.generate_npc(commoner=True, gender='Male')
print malecom 
print