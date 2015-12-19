class Action:
	__init__(self):
		pass
	def checkTargets(self, performer, targets):
		for target in targets:
			if target.getGlobalTrait['guarded']:
				return True
		return False
	def checkPerformer(self, performer):
		return performer.getGlobatTrait['blocked']
	def do(self, performer, targets):
		# This is where the specific action will take place for subclasses.
		return True
	def perform(self, performer, targets):
		if self.checkPerformer(self, performer):
			performer.addMsg('You were blocked.')
		elif self.checkTargets(performer, targets):
			performer.addMsg('One of your targets was guarded.')
		elif self.do(self, performer, targets):
			performer.addMsg('Your action was successful!')
		else:
			performer.addMsg('Your action failed.')