from PlayerManager import *
import processes.SetupGame as SetupGame
import processes.DayActions as DayActions
import processes.VoteResolver as VoteResolver
from components.DayActions import DayActions as DayActComp

def spoofSetup(pm):
    p1 = pm.createPlayer()
    pm.setComponent(p1, 'name', 'brad')
    pm.setComponent(p1, DayActComp.typeName, DayActComp(['vote']))

    p2 = pm.createPlayer()
    pm.setComponent(p2, 'name', 'fred')
    pm.setComponent(p2, DayActComp.typeName, DayActComp(['vote']))

pm = PlayerManager()
#SetupGame.process(pm)
spoofSetup(pm)
DayActions.process(pm)
VoteResolver.process(pm)
