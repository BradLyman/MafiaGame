from gameInitialization import *

# Take a list of (player, action, targets, priority) tuples.  Preime the players to do their actions, and retrun a dict of actions sorted by priority.
def primeActions(actionInfoList):
	actionDict = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : []}
	for info in actionInfoList:
		(player, action, targets, priority) = info
		# Pass validTargets, rather than all players below.
		player.currentAction = action
		player.traits['targets'] = targets
		actionDict[priority] += [player]
	return actionDict

# Return a list of players, ordered by action priority, shuffling within each priority.
def orderPlayers(actionDict):
	actionOrderPlayers = []
	for i in range(0, 7):
		nextActions = actionDict[i]
		if nextActions:
			shuffle(nextActions)
			actionOrderPlayers += nextActions
	return actionOrderPlayers
	
# Have each player perform its action.
def doActions(players):
	for player in players:
		player.takeAction()