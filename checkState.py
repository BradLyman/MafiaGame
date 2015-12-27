from getAndDoActions import *
import Globals

# Get a list of living threats.
def getLivingThreats(teams):
	threats = []
	for team in teams:
		if team.isThreat:
			if team.getLivingPlayers():
				threats += [team]
	return threats

# Get all teams (living or not), that are not threats.
def getNonThreats(teams):
	nonThreats = []
	for team in teams:
		if not team.isThreat:
			nonThreats += [team]
	return nonThreats

# Return a list of teams that won.
def checkWinners(teams, players):
	totalAlive = len(getSpecificPlayers(players, {'alive' : True}))
	threats = getLivingThreats(teams)
	totalThreats = len(threats)
	if totalThreats > 1:
		return False
	elif totalThreats == 1:
		# A threatening team wins if it is the only threatening team, and other players cannot form a majority.
		if 2*threats[0].getLivingPlayers() >= totalAlive:
			return threats
		else:
			return False
	else:
		# All non-threatening teams win if the threats are eliminated.
		return getNonThreats(teams)

# Display all teams in list, and the members of those teams.
def displayTeams(teams):
	for i, team in enumerate(teams):
		print('(#%s) %s' % (i + 1, team.name))
		for j, player in enumerate(team.members):
			print('\t(#%s) %s' % (j + 1, player.name))

# Remove all traits, besides the 'name' trait.
def cleanUpGlobalTraits(players):
	Globals.globalPlayerTraits = []
	for player in players:
		Globals.globalPlayerTraits += [{'name' : player.name}]