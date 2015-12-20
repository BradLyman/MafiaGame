from PlayerManager import *
import processes.SetupGame as SetupGame
import processes.DayActions as DayActions
import processes.VoteResolver as VoteResolver

def spoofSetup(pm):
    p1 = pm.createPlayer()
    pm.setComponent(p1, 'name', 'brad')

    p2 = pm.createPlayer()
    pm.setComponent(p2, 'name', 'fred')

pm = PlayerManager()
#SetupGame.process(pm)
spoofSetup(pm)
DayActions.process(pm)
VoteResolver.process(pm)
