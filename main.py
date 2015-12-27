from gameInitialization import *
from getAndDoActions import *
from checkState import *
from voting import *
import Globals




(teams, players) = startGame()
Day = False
for team in teams:
	team.cleanUp()
cleanUpGlobalTraits(players)
while True:
	alivePlayers = getSpecificPlayers(players, {'alive' : True})
	if Day:
		getVotes(alivePlayers)
		voteCountList = countVotes(alivePlayers)
		displayVotes()
		killTopVoted(voteCountList)
		Day = False
	else:
		actionDict = getActions(alivePlayers)
		actionSequence = orderActions(actionDict)
		doActions(actionSequence)
		for team in teams:
			team.cleanUp()
		cleanUpGlobalTraits(players)
		Day = True
	winners = checkWinners(teams, players)
	if winners:
		print('The winners are:')
		displayTeams(winners)
		break