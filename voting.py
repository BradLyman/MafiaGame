import Globals
from getAndDoActions import *
from gameInitialization import *

# Provide a list of players, and get a vote.
def promptForVote(player, playerList):
	print('%s, who are you voting for?')
	print('(0) Do Not Vote')
	displayPlayers(playerList)
	voteIndex = getIntOrFalse('Choose a player:  ', maximum = len(playerList))
	if voteIndex:
		return playerList[voteIndex - 1]
	else:
		return False

# Apply a player's vote to the global player trait list.
def getVotes(playerList):
	for player in playerList:
		vote = promptForVote(player, playerList)
		if vote:
			player.voteFor(vote)

# Count the votes in the global player trait list.
def countVotes(playerList):
	voteCountList = []
	for player in playerList:
		voters = player.getGlobalTrait('voters')
		if voters:
			count = len(voters)
		else:
			count = 0
		voteCountList += [(player, count)]
	return voteCountList

# If a player has the majority of votes, kill it.
def killTopVoted(voteCountList):
	halfPlayers = len(voteCountList)/2
	for voteCount in voteCountList:
		if voteCount[1] > halfPlayers:
			print('%s was voted off!' % voteCount[0].name)
			voteCount[0].traits['alive'] = False
			break
	else: print('No one was voted off.')

# Print all players receiving votes, and the players that voted for them.
def displayVotes():
	print('Voting results:')
	for player in Globals.globalPlayerTraits:
		try: voters = player['voters']
		except: voters = False
		if voters:
			total = len(voters)
			voteString = buildStringFromList(voters)
			print('%s (%s): %s' % (player['name'], total, voteString))
