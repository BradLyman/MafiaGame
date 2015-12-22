class Action:
	def __init__(self):
		pass
	def validateTargets(self, targets):
		assert len(targets) == self.totalTargets, 'Invalid number of targets.  Expected: %s, Actual: %s' % (self.totalTargets, len(targets))
	def checkTargets(self, performer, targets):
		for target in targets:
			if target.getGlobalTrait('guarded'):
				return True
		return False
	def checkPerformer(self, performer):
		return performer.getGlobalTrait('blocked')
	def do(self, performer, targets):
		# This is where the specifiquit()c action will take place for subclasses.
		return True
	def perform(self, performer, targets):
		self.validateTargets(targets)
		if self.checkPerformer(performer):
			performer.addMsg('You were blocked.')
		elif self.checkTargets(performer, targets):
			performer.addMsg('One of your targets was guarded.')
		elif self.do(performer, targets):
			performer.addMsg('Your action was successful!')
		else:
			performer.addMsg('Your action failed.')

class Vigilence(Action):
	def __init__(self):
		self.totalTargets = 1
		super().__init__()
	def checkTargets(self, performer, targets):
		# You can be vigilent against a target, even if they are guarded.
		return False
	def do(self, performer, targets):
		performer.traits['vigilent'] = targets[0]
		return super().do(performer, targets)

class MafiaHit(Action):
	def __init__(self):
		self.totalTargets = 1
		super().__init__()
	def perform(self, performer, targets):
		if performer.Team.killsLeft < 1:
			performer.addMsg('Your team has no more kills left this turn.')
			return False
		else:
			performer.Team.killsLeft -= 1
			super().perform(performer, targets)
	def do(self, performer, targets):
		return targets[0].killBy(performer)