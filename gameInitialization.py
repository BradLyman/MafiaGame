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

# Ensure an integer (within range) is returned from an input prompt.  Otherwise, return False.
def getIntOrFalse(message, minimum = 0, maximum = False):
	value = input(message)
	try:
		value = int(value)
	except:
		return False
	else:
		if not maximum:
			maximum = value
		if minimum <= value <= maximum:
			return value
		else:
			print('Invalid input!')
			return False

# Return True or False, based on input of "y" or "n".
def getYesOrNo(message):
	while True:
		response = input(message)
		if response == 'y':
			return True
		elif response == 'n':
			return False
		else:
			print('Invalid input!')

# Convert the role list from dict (used for display purposes) to a list of (role, team) tuples.
def rolesDictToList(usedRoles, team):
	listRoles = []
	for key in usedRoles:
		listRoles += [(key, team)] * usedRoles[key]
	return listRoles

# Prompt the user to choose roles and the quantity of each.
def getListOfTeamRoles(team):
	usedRoles = {}
	while True:
		print('Select roles for team "%s".' % team.name)
		displayRolesDesc(availableRoles)
		selection = getIntOrFalse('(Leave blank to start game):  ')
		if not selection:
			return rolesDictToList(usedRoles, team)
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

# Create and name a list of teams
def createTeams():
	teams = []
	while True:
		newTeamName = input("What is team %s's name?  Leave blank to finish team creation.  " % (len(teams) + 1))
		if not newTeamName: break
		isThreat = getYesOrNo('Is this team a threat? (y/n):  ')
		killsPerTurn = getIntOrFalse('How many kills per night are available to this team?  ')
		collaborative = getYesOrNo('Can this team collaborate? (y/n):  ')
		teams += [Team(newTeamName, collaborative, isThreat, killsPerTurn)]
	return teams

def getRoles(teams):
	listRoles = []
	for i in teams:  #ha!
		listRoles += getListOfTeamRoles(i)
	return listRoles

# Take a list of (role, team) tuples, and create players on those teams.
def addPlayersToTeams(listRoles):
	shuffle(listRoles)
	playerList = []
	for i, pair in enumerate(listRoles):
		name = input('Player %s, what is your name?  ' % (i + 1))
		playerList += [pair[1].createPlayer(pair[0], name)]
	return playerList

# Builds a string from a list.  Only uses a deliminator if 2 or more items.
def buildStringFromList(inputList, deliminator = ', ', finalDelim = ', and '):
	outputString = ''
	totalItems = len(inputList)
	for i, item in enumerate(inputList):
		try:
			item = item.name
		except:
			pass
		if i == 0:
			outputString = item
		elif totalItems == i + 1:
			outputString += finalDelim + item
		else:
			outputString += deliminator + item
	return outputString

# Start the game!  Return a list of teams, and a list of players (in order of sign-up)
def startGame():
	teams = createTeams()
	roles = getRoles(teams)
	players = addPlayersToTeams(roles)
	return (teams, players)