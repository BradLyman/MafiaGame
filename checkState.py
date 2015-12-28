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

# Remove all traits, besides the 'name' trait.
def cleanUpGlobalTraits(players):
	Globals.globalPlayerTraits = []
	for player in players:
		Globals.globalPlayerTraits += [{'name' : player.name}]

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