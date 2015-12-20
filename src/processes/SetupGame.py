from util import getIntInput
from components.DayActions import DayActions as DayActionsComp

def _promptName(pId):
    return input(
        "Please enter name for player {}:  ".format(pId)
    )

def _setupPlayer(pm, pId):
    name = _promptName(pId)
    pm.setComponent(pId, 'name', name)

    actions = DayActionsComp(['vote'])
    pm.setComponent(pId, DayActionsComp.typeName, actions)


def process(pm):
    playerCount = getIntInput(
        "How many people will be playing?\n",
        0, 100
    )
    for i in range(0, playerCount):
        pId  = pm.createPlayer()
        _setupPlayer(pm, pId)

    print('Finished setting up {} players'.format(playerCount))
