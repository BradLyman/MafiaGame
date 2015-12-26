from gameInitialization import *

# return a list of players that meet requirements (dict).
def getSpecificPlayers(playerList, requirements):
	matches =[]
	for player in playerList:
		include = True
		for key in requirements:
			# Include the player if the desired trait is found in either the global dict, or the player's dict.
			include = (requirements[key] == player.traits[key] or requirements[key] == player.getGlobalTrait(key))
			if not include: break
		if include:
			matches += [player]
	return matches

# Display a numbered list of players.
def displayPlayers(playerList):
	for i, player in enumerate(playerList):
		print('(%s) %s' % (i, player.name))

# Display a numbered list of actions.
def displayActions(player):
	print('Actions Available for %s:' % player.name)
	for i, action in enumerate(player.actions):
		print('(%s) %s - \r\n\t%s' % (i + 1, action.name, action.description))

# Prompt the thplayer for an action choice, and a choice of target(s).
def promptPlayerForAction(player,playerList):
	targets = []
	displayActions(player)
	indexAction = getIntOrFalse('Which Action will you perform?  (Leave blank to pass this turn)')
	if not choice: return targets, player.actions[0]
	else: indexAction -= 1
	action = player.actions[indexAction]
	priority = action.priority
	for i in range(1, action.totalTargets + 1):
		validTargets = getSpecificPlayers(playerList, action.targetRequirements)
		displayPlayers(validTargets)
		indexTarget = getIntOrFalse('Who is target # %s?  ' % i)
		targets += [validTargets[indexTarget]]
	return targets, action, priority

# Create a list of players, ordered by action priority, shuffling within each priority.
def orderActions(actionDict):
	inOrder = []
	for i in range(0, 7):
		nextActions = actionDict[i]
		if nextActions:
			shuffle(nextActions)
			inOrder += nextActions
	return inOrder

# Have each player perform its action.
def doActions(players):
	for player in players:
		player.takeAction()

# Get action selections from each player.  Return a dict with each player in a priority bucket.
def getActions(players):
	actionDict = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : []}
	for player in players:
		(targets, action, priority) = promptPlayerForAction(player, players)
		player.currentAction = action
		player.traits['targets'] = targets
		actionDict[priority] += [player]
	return actionDict