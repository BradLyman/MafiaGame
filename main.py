from gameInitialization import *
from getAndDoActions import *
from checkState import *
import Globals




(teams, players) = startGame()
while True:
	actionDict = getActions(players)
	actionSequence = orderActions(actionDict)
	doActions(actionSequence)
	for team in teams:
		team.cleanUp()
	winners = checkWinners(teams, players)
	if winners:
		print('The winners are:')
		displayTeams(winners)
		break