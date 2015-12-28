import Globals
from getAndDoActions import *
from gameInitialization import *

# Take a list of (voter, votee) tuples, and apply votes.
def applyVotes(voteInfoList):
	for info in voteInfoList:
		info[0].voteFor(info[1])

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
			voteCount[0].traits['alive'] = False
			return voteCount[0]
	return False