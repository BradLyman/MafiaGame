from gameInitialization import *
from getAndDoActions import *
from checkState import *
from voting import *
from displayAndPrompt import *
import Globals

teamInfoList = promptTeams()
teams = createTeams(teamInfoList)
roleList = []
for team in teams:
	roleList += getListOfTeamRoles(team)
playerInfoList = getPlayerNames(roleList)	
players = addPlayersToTeams(playerInfoList)
Day = False
for team in teams:
	team.cleanUp()
cleanUpGlobalTraits(players)
while True:
	alivePlayers = getSpecificPlayers(players, {'alive' : True})
	if Day:
		voteInfoList = getVotes(alivePlayers)
		applyVotes(voteInfoList)
		voteCountList = countVotes(alivePlayers)
		displayVotes()
		killedOff = killTopVoted(voteCountList)
		displayKilledOff(killedOff)
		Day = False
	else:
		actionInfoList = getActions(alivePlayers)
		actionDict = primeActions(actionInfoList)
		actionOrderPlayers = orderPlayers(actionDict)
		doActions(actionOrderPlayers)
		for team in teams:
			team.cleanUp()
		cleanUpGlobalTraits(players)
		Day = True
	winners = checkWinners(teams, players)
	if winners:
		print('The winners are:')
		displayTeams(winners)
		break