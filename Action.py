class Action:
	def __init__(self):
		self.targetRequirements = {'alive' : True}
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
		# This is where the specific action will take place for subclasses.
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


# Priorities:
#	(0) Thumb - twiddling
#	(1) Generic Blocking
#	(2) Kill Protection
#	(3) Kills
#	(4) Information-Gathering
#	(5) Saves


class Vigilence(Action):
	def __init__(self):
		self.name = 'Vigilence'
		self.description = 'You are protected if your target tries to kill you.'
		self.totalTargets = 1
		self.priority = 2
		super().__init__()
	def checkTargets(self, performer, targets):
		# You can be vigilent against a target, even if they are guarded.
		return False
	def do(self, performer, targets):
		performer.traits['vigilent'] = targets[0]
		return super().do(performer, targets)

class TakeOut(Action):
	def __init__(self):
		self.name = 'Take Out'
		self.description = 'Kill a Player.'
		self.totalTargets = 1
		self.priority = 3
		super().__init__()
	def perform(self, performer, targets):
		if performer.team.killsLeft < 1:
			performer.addMsg('Your team has no more kills left this turn.')
			return False
		else:
			performer.team.killsLeft -= 1
			super().perform(performer, targets)
	def do(self, performer, targets):
		return targets[0].killBy(performer)

class DoNothing(Action):
	def __init__(self):
		self.name = 'Do Nothing'
		self.description = 'You do not do anything this phase.'
		self.totalTargets = 0
		self.priority = 0
	def do(self, performer, targets):
		performer.addMsg('Your thumbs are tired, from all the twiddling!')
		return True