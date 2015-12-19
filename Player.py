class Player:
	__init__(self, name):
		self.traits = {'alive' : True, 'targets' : []}
		self.actions = [] 		# To be filled with "Action" objects
		self.name = name
		self.currentAction = -1
		self.msg = ''
		self.log = []
	def getGlobalTrait(self, trait):
		for player in globalPlayerTraits:
			if self.name == player['name']:
				return player[trait]
		# It is important to note, that a trait will return False, if it doesn't exist
		return False
	def addMsg(self, newMsg):
		self.msg += newMsg + '/r/n'
	def killBy(self, killer):
		self.traits['alive'] = False
		return True
	def investigateBy(self, investigator, trait):
		if trait in self.traits:
			return self.traits[trait]
		else getGlobalTrait(self, trait):
			# This will return False if trait not present.
			return getGlobalTrait(self, trait) 
	def takeAction(self):
		if self.currentAction >= 0:
			self.addMsg('No action taken.')
			return
		else:
			# The action will check if the target is guarded, or if performer is blocked.
			self.actions[self.currentAction].perform(performer = self, targets = self.traits['targets'])
	def cleanUp(self):
		self.traits['targets'] = []
		self.currentAction = -1
		self.log += self.msg
		self.msg = ''