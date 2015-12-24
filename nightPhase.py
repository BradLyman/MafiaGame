from gameInitialization import *

# return a list of players that meet requirements (dict).
def getSpecificPlayers(playerList, requirements):
	matches =[]
	for player in playerList:
		include = True
		for key in requirements:
			# Include the player if the desired trait is found in either the global dict, or the player's dict.
			include = (requirements[key] == player.traits[key] or requirements[key] == player.getGlobalTrait[key])
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
