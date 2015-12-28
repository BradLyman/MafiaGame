from Player import *
from random import shuffle, choice
import Globals

# Take a (role, team, player name) tuple list, and create those players.
def addPlayersToTeams(nameList):
	players = []
	for item in nameList:
		players += [item[1].createPlayer(item[0], item[2])]
	return players

# Return a list of teams created from (team name, isCollaborative, isThreat, killsPerTurn) tuples.
def createTeams(teamInfoList):
	teams = []
	for info in teamInfoList:
		teams += [Team(*info)]
	return teams