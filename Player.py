from Action import *
import Globals

class Player:
	def __init__(self, name):
		self.traits = {'alive' : True, 'targets' : []}
		self.actions = [] 		# To be filled with "Action" objects
		self.name = name
		self.currentAction = -1
		self.msg = ''
		self.log = []
	def getGlobalTrait(self, trait):
		for player in Globals.globalPlayerTraits:
			if self.name == player['name']:
				try: return player[trait]
				except: return False
		# It is important to note, that a trait will return False, if it doesn't exist
		return False
	def addMsg(self, newMsg):
		self.msg += newMsg + '\r\n'
	def killBy(self, killer):
		self.traits['alive'] = False
		return True
	def investigateBy(self, investigator, trait):
		if trait in self.traits:
			return self.traits[trait]
		else:
			# This will return False if trait not present.
			return self.getGlobalTrait(trait)
	def takeAction(self):
		if self.currentAction < 0:
			self.addMsg('No action taken.')
			return
		else:
			# The action will check if the target is guarded, or if performer is blocked.
			self.actions[self.currentAction].perform(performer = self, targets = self.traits['targets'])
	def cleanUp(self):
		self.traits['targets'] = []
		self.currentAction = -1
		self.log += [self.msg]
		self.msg = ''

class Citizen(Player):
	title = 'Citizen'
	description = 'A good guy who has a chance to protect himself.'
	def __init__(self, name):
		super().__init__(name)
		self.traits['allegience'] = 'Town'
		self.traits['vigilent'] = False
		self.actions += [Vigilence()]
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
	title = 'Mafian'
	description = 'A bad guy.  One bad guy can kill per turn.'
	def __init__(self, name):
		super().__init__(name)
		self.traits['allegience'] = 'Mafia'
		self.actions += [MafiaHit()]
	def cleanUp(self):
		MafiaHit.alreadyDone = False
		super().cleanUp()