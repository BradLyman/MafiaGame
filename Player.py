from Action import *
import Globals

# The Team class holds Players together that are on the same team.
class Team:
	def __init__(self, name, collaborative = False, isThreat = False, killsPerTurn = 0):
		self.members = []
		self.killsLeft = killsPerTurn
		self.killsPerTurn = killsPerTurn
		self.isThreat = isThreat
		self.name = name
		self.collaborative = collaborative
	# Add an existing player to this team.
	def addPlayer(self, player):
		self.members += player
		player.team = self
		player.addMsg('You were added to %s.' % self.name)
	# Create a new player, then add it to this team.
	def createPlayer(self, role, name):
		newPlayer = role(name)
		self.members += [newPlayer]
		# The two items below I may add in the __init__ of the player class.
		newPlayer.team = self
		newPlayer.traits['allegience'] = self.name
		newPlayer.addMsg('You were added to %s.' % self.name)
		return newPlayer
	# Get the number of living players on this team.
	def getLivingPlayers(self):
		living = 0
		for member in self.members:
			if member.traits['alive']:
				living += 1
		return living
	# Reset kills, but also run the cleanUp on team members.
	def cleanUp(self):
		self.killsLeft = self.killsPerTurn
		for player in self.members:
			player.cleanUp()

# The Player class represents the users of the game, and has methods for the various actions those users can take.
class Player:
	def __init__(self, name):
		self.traits = {'alive' : True, 'targets' : []}
		self.actions = [DoNothing()] 		# To be filled with "Action" objects
		self.name = name
		self.currentAction = self.actions[0]
		self.msg = ''
		self.log = []
		self.team = Team('Independent')
		Globals.globalPlayerTraits += [{'name' : name}]
	# This method looks in the global dict for this player, returning False if the trait does nto exist.
	def getGlobalTrait(self, trait):
		for player in Globals.globalPlayerTraits:
			if self.name == player['name']:
				try: return player[trait]
				except: return False
		return False
	def setGlobalTrait(self, trait, value):
		for player in Globals.globalPlayerTraits:
			if self.name == player['name']:
				player[trait] = value
				break
	def addMsg(self, newMsg):
		self.msg += newMsg + '\r\n'
	# This method kills the player.  Subclasses may handle this differently.
	def killBy(self, killer):
		self.traits['alive'] = False
		self.addMsg('You were killed.')
		return True
	# This method returns the requested trait, either in the global dict, or the local self.traits.
	def investigateBy(self, investigator, trait):
		if trait in self.traits:
			return self.traits[trait]
		else:
			# This will return False if trait not present.
			return self.getGlobalTrait(trait)
	# Perform the action selected, if able.
	def takeAction(self):
		targets = self.traits['targets']
		targetString = ''
		for target in targets:
			if targetString:
				targetString += ' & ' + target.name
			else:
				targetString = target.name
		self.addMsg('You tried to use %s on %s.' % (self.currentAction.name, targetString))
		self.currentAction.perform(performer = self, targets = targets)
	# Should run after every round.  Moves messages to log, then clears the log.
	def cleanUp(self):
		self.traits['targets'] = []
		self.currentAction = self.actions[0]
		self.log += [self.msg]
		self.msg = ''
	# Return a list of teammates, excluding self.
	def getTeammates(self):
		teammates = []
		for teammate in self.team.members:
			if teammate != self:
				teammates += [teammate]
		return teammates
	# Add this player's name to the list of players voting for target.
	def voteFor(self, player):
		currentVotes = player.getGlobalTrait('voters')
		if currentVotes:
			currentVotes += [self]
		else:
			currentVotes = [self]
		player.setGlobalTrait('voters', currentVotes)
		self.addMsg('You voted for %s.' % player.name)
		player.addMsg('%s voted for you.' % self.name)


class Citizen(Player):
	title = 'Citizen'
	description = 'Can protect himself, if he can pick the player trying to kill him.'
	def __init__(self, name):
		super().__init__(name)
		self.traits['vigilent'] = False
		self.actions += [Vigilence()]
	# Adjusted from parent to protect player if he correctly picked his killer.
	def killBy(self, killer):
		if killer == self.traits['vigilent']:
			self.addMsg('Your vigilence saved you from %s!' % killer.name)
			return False
		else:
			return super().killBy(killer)
	def cleanUp(self):
		self.traits['vigilent'] = False
		super().cleanUp()

class Mafian(Player):
	title = 'Killer'
	description = 'Can Kill.'
	def __init__(self, name):
		super().__init__(name)
		self.actions += [TakeOut()]