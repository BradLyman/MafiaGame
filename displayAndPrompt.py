from checkState import *
from Player import *
from Action import *
from random import shuffle

availableRoles = [Citizen, Mafian]


### GENERIC PROMPTS ###


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

# Display a numbered list of players.
def displayPlayers(playerList):
	for i, player in enumerate(playerList):
		print('(%s) %s' % (i + 1, player.name))

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

# Display all teams in list, and the members of those teams.
def displayTeams(teams):
	for i, team in enumerate(teams):
		print('(#%s) %s' % (i + 1, team.name))
		for j, player in enumerate(team.members):
			print('\t(#%s) %s' % (j + 1, player.name))


### GAME INITIALIZATION PROMPTS ###


# Prompt to get a list of (team name, isCollaborative, isThreat, killsPerTurn) tuples.
def promptTeams():
	teamInfoList = []
	while True:
		newTeamName = input("What is team %s's name?  Leave blank to finish team creation.  " % (len(teamInfoList) + 1))
		if not newTeamName: break
		isThreat = getYesOrNo('Is this team a threat? (y/n):  ')
		killsPerTurn = getIntOrFalse('How many kills per night are available to this team?  ')
		isCollaborative = getYesOrNo('Can this team collaborate? (y/n):  ')
		teamInfoList += [(newTeamName, isThreat, isCollaborative, killsPerTurn)]
	return teamInfoList

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

# Take a list of (role, team) tuples, and add player names.  Retrun (role, team, player name).
def getPlayerNames(roleList):
	shuffle(roleList)
	playerInfoList = []
	for i, pair in enumerate(roleList):
		name = input('Player %s, what is your name?  ' % (i + 1))
		playerInfoList += [(pair[0], pair[1], name)]
	return playerInfoList

# Print the title & description of a list of roles.
def displayRolesDesc(roles):
	for i, role in enumerate(roles):
		print('(%s) %s - \r\n\t%s' % (i + 1, role.title, role.description))

# Convert the role list from dict (used for display purposes) to a list of (role, team) tuples.
def rolesDictToList(usedRoles, team):
	listRoles = []
	for key in usedRoles:
		listRoles += [(key, team)] * usedRoles[key]
	return listRoles

# Print the roles (and quantity of each) in the 'usedRoles' dict.
def displayRolesQty(usedRoles):
	for role in usedRoles:
		print('%s: %s' % (role.title, usedRoles[role]))


### VOTING PROMPTS ###


# Get player votes, returning a (voter, votee) tuple.
def getVotes(playerList):
	voteInfoList = []
	for voter in playerList:
		votee = promptForVote(voter, playerList)
		if votee:
			voteInfoList += [(voter, votee)]
	return voteInfoList

# Provide a list of players, and get a vote.
def promptForVote(player, playerList):
	print('%s, who are you voting for?')
	print('(0) Do Not Vote')
	displayPlayers(playerList)
	voteIndex = getIntOrFalse('Choose a player:  ', maximum = len(playerList))
	if voteIndex:
		return playerList[voteIndex - 1]
	else:
		return False

# Print all players receiving votes, and the players that voted for them.
def displayVotes():
	print('Voting results:')
	for player in Globals.globalPlayerTraits:
		try: voters = player['voters']
		except: voters = False
		if voters:
			total = len(voters)
			voteString = buildStringFromList(voters)
			print('%s (%s): %s' % (player['name'], total, voteString))

# Display the voting results.
def displayKilledOff(killedOff):
	if killedOff:
		print('%s has been voted off!' % killedOff.name)
	else:
		print('No one was voted off...')


### NIGHT ACTION PROMPTS ###


# Get action selections from each player.  Return a list of (player, action, targets, priority) tuples.
def getActions(players):
	actionInfoList = []
	for player in players:
		### Still need to define valid targets here.  How do I do that when targets is action dependent? ###
		(targets, action, priority) = promptPlayerForAction(player, players)
		actionInfoList += [(player, action, targets, priority)]
	return actionInfoList

# Prompt the thplayer for an action choice, and a choice of target(s).
def promptPlayerForAction(player, validTargets):
	targets = []
	print('---You belong to %s---' % player.team.name)
	displayTeammates(player)
	displayLog(player)
	displayActions(player)
	indexAction = getIntOrFalse('Which Action will you perform?  (Leave blank to pass this turn)', maximum = len(player.actions))
	if not indexAction: return targets, player.actions[0], 0
	else: indexAction -= 1
	action = player.actions[indexAction]
	priority = action.priority
	for i in range(1, action.totalTargets + 1):
		displayPlayers(validTargets)
		indexTarget = getIntOrFalse('Who is target # %s?  ' % i, maximum = len(validTargets))
		targets += [validTargets[indexTarget - 1]]
	return targets, action, priority

# If the player belongs to a collaborative team, display his teammates.
def displayTeammates(player):
	if player.team.collaborative:
		print('Your teammates are:')
		for i, teammate in enumerate(player.getTeammates()):
			if teammate.traits['alive']: status = ''
			else: 						 status = '  (DEAD)'
			print('(%s) %s%s' % (i + 1, teammate.name, status))

# Prints the player's log, separating each day by line.
def displayLog(player):
	for i, line in enumerate(player.log):
		print('--Night %s--' % i)
		print(line)

# Display a numbered list of actions.
def displayActions(player):
	print('Actions Available for %s:' % player.name)
	for i, action in enumerate(player.actions):
		print('(%s) %s - \r\n\t%s' % (i + 1, action.name, action.description))