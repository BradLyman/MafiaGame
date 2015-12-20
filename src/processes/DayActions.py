from util import getInputInSeq
from components.DayActions import DayActions as DayActionsComp
import processes.actions.Directory as Dir

def _createPromptString(dayActsComp):
    actions = dayActsComp.actions

    promptString = "Choose an action:\n"
    for action in actions:
        promptString += "-> {}\n".format(action)

    return promptString


def _runPlayerAction(pId, dayActsComp, pm):
    promptString = _createPromptString(dayActsComp)
    result       = False

    while (not result):
        choice     = getInputInSeq(promptString, dayActsComp.actions)
        actionName = dayActsComp.actions[choice]

        result = Dir.actionDirectory[actionName](pId, pm)


def process(pm):
    dayActDirectory = pm.getComponentDirectory(DayActionsComp.typeName)

    for pId, dayActsComp in dayActDirectory.items():
        _runPlayerAction(pId, dayActsComp, pm)
