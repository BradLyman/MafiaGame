from util import getIntInput

def _promptName(pId):
    return input(
        "Please enter name for player {}:  ".format(pId)
    )

def process(pm):
    playerCount = getIntInput(
        "How many people will be playing?\n",
        0, 100
    )
    for i in range(0, playerCount):
        pId  = pm.createPlayer()
        name = _promptName(pId)
        pm.setComponent(pId, 'name', name)
    print('Finished setting up {} players'.format(playerCount))
