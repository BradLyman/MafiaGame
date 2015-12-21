from Player import *
from random import shuffle, choice
import Globals

availableRoles = [Citizen, Mafian]

# Print the title & description of a list of roles.
def displayRolesDesc(roles):
	for i, role in enumerate(roles):
		print('(%s) %s - \r\n\t%s' % (i + 1, role.title, role.description))

# Print the roles (and quantity of each) in the 'usedRoles' dict.
def displayRolesQty(usedRoles):
	for role in usedRoles:
		print('%s: %s' % (role.title, usedRoles[role]))

# Ensure an integer is returned from an input prompt.  A False will be handled.
def getIntOrFalse(message):
	value = input(message)
	try: return int(value)
	except: return False

# Convert the role list from dict (used for display purposes) to a shuffled list.
def rolesDictToList(usedRoles):
	listRoles = []
	for key in usedRoles:
		listRoles += [key] * usedRoles[key]
	shuffle(listRoles)
	return listRoles

# Prompt the user to choose roles and the quantity of each.
def getListOfRoles():
	usedRoles = {}
	while True:
		print('Select a role to be in the game:')
		displayRolesDesc(availableRoles)
		selection = getIntOrFalse('(Leave blank to start game):  ')
		if not selection:
			return rolesDictToList(usedRoles)
		selectedRole = availableRoles[selection - 1]
		qty = getIntOrFalse('How many %ss would you like?\r\n(Leave blank to pick a different role):  ' % selectedRole.title)
		if not qty: continue
		# Build a dict of (role : quantity) pairs.  If role is already in dict, add to existing quantity.
		try:
			usedRoles[selectedRole] += qty
		except:
			usedRoles[selectedRole] = qty
		print('Current Roles:')
		displayRolesQty(usedRoles)

# Create Players for each of the roles chosen in getListOfRoles.  Prompt user for a name for each Player.
def createPlayerList(listRoles):
	playerList = []
	for i, role in enumerate(listRoles):
		newName = input("What is Player %s's name?  " % (i + 1))
		playerList += [role(newName)]
	return playerList
