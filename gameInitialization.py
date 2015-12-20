from Player import *
import Globals

def displayRolesDesc(roles):
	for i, role in enumerate(roles):
		print('(%s) %s - \r\n\t%s' % (i + 1, role.title, role.description))

def displayRolesQty(usedRoles):
	for role in usedRoles:
		print('%s: %s' % (role.title, usedRoles[role]))

def getIntOrFalse(message):
	value = input(message)
	try: return int(value)
	except: return False

def getListOfRoles():
	availableRoles = [Citizen, Mafian]
	usedRoles = {}
	while True:
		print('Select a role to be in the game:')
		displayRolesDesc(availableRoles)
		selection = getIntOrFalse('(Leave blank to start game):  ')
		if not selection: return usedRoles
		selectedRole = availableRoles[selection - 1]
		qty = getIntOrFalse('How many %ss would you like?\r\n(Leave blank to pick a different role):  ' % selectedRole.title)
		if not qty: continue
		try:
			usedRoles[selectedRole] += qty
		except:
			usedRoles[selectedRole] = qty
		print('Current Roles:')
		displayRolesQty(usedRoles)