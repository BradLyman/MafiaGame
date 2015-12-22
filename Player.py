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
	# Add an existing player to this team.
	def addPlayer(self, player):
		self.members += player
		player.team = self
	# Create a new player, then add it to this team.
	def createPlayer(self, role, name):
		newPlayer = role(name)
		self.members += [newPlayer]
		# The two items below I may add in the __init__ of the player class.
		newPlayer.team = self
		newPlayer.traits['allegience'] = self.name
		return newPlayer
	# Get the number of living players on this team.
	def getLivingPlayers(self):
		living = 0
		for member in self.members:
			if member.traits['alive']:
				living += 1
		return living
	def cleanUp(self):
		self.killsLeft = self.killsPerTurn

# The Player class represents the users of the game, and has methods for the various actions those users can take.
class Player:
	def __init__(self, name):
		self.traits = {'alive' : True, 'targets' : []}
		self.actions = [] 		# To be filled with "Action" objects
		self.name = name
		self.currentAction = -1
		self.msg = ''
		self.log = []
		self.team = Team('Independent')
	# This method looks in the global dict for this player, returning False if the trait does nto exist.
	def getGlobalTrait(self, trait):
		for player in Globals.globalPlayerTraits:
			if self.name == player['name']:
				try: return player[trait]
				except: return False
		return False
	def addMsg(self, newMsg):
		self.msg += newMsg + '\r\n'
	# This method kills the player.  Subclasses may handle this differently.
	def killBy(self, killer):
		self.traits['alive'] = False
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
		if self.currentAction < 0:
			self.addMsg('No action taken.')
			return
		else:
			# The action will check if the target is guarded, or if performer is blocked.
			self.actions[self.currentAction].perform(performer = self, targets = self.traits['targets'])
	# Should run after every round.  Moves messages to log, then clears the log.
	def cleanUp(self):
		self.traits['targets'] = []
		self.currentAction = -1
		self.log += [self.msg]
		self.msg = ''

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