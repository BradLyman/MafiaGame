from Components import DayActions
from util import getIntInput

def process(pm):
    players = pm.getPlayersWithComponent(DayActions)
    for pId in players:
        getActionChoice(players[pId])

def getActionChoice(actions):
    actionChoiceStr = ""
    index = 0
    for actionName in actions.actionNames:
        actionChoiceStr += (
            "{}) {}".format(index, actionName)
        );
        index += 1
    actionChoiceStr += "-\n"
    print(actionChoiceStr)
    choice = getIntInput(
        actionChoiceStr,
        0,
        len(actions.actionNames)-1
    )
