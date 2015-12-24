from nightPhase import *
from gameInitialization import *
import Globals




(teams, players) = startGame()
actionDict = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : []}
for player in players:
	(targets, action, priority) = promptPlayerForAction(player, players)
	player.currentAction = action
	player.traits['targets'] = targets
	actionDict[priority] += [player]
actionSequence = orderActions(actionDict)
doActions(actionSequence)