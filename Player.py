class Player:
	__init__(self, name):
		self.attributes = {'alive' : True}
		self.actions = [] 		# To be filled with "Action" objects
		self.name = name
		self.currentAction = -1
		self.message =''
	def addMsg(self, newMsg):
		self.message += newMsg + '/r/n'
	def killBy(self, killer):
		self.attributes['alive'] = False
		return True
	def investigateBy(self, investigator, trait):
		if trait in self.attributes:
			return self.attributes[trait]
		elif trait in playersglobaltraits: # to be created later
			pass
			return False
		else:
			return False
	def takeAction(self):
		if self.currentAction >= 0:
			self.addMsg('No action taken.')
			return
		self.actions[self.currentAction].execute(self, 'targets' = self.attributes['targets'])