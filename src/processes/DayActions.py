from util import getIntInputInSeq
from components.Vote import Vote

def _getPlayerVoteChoice(nameDirectory):
    promptString = "Enter a number to select the player target\n";
    for pId, name in nameDirectory.items():
        promptString += "  {}) {}\n".format(pId, name)
    promptString += "\n>"

    return getIntInputInSeq(promptString, list(nameDirectory.keys()))

def process(pm):
    nameDirectory = pm.getComponentDirectory('name');

    # ask each player who they vote to lynch
    for pId, name in nameDirectory.items():
        print("{} who will you vote to kill?".format(name))
        target = _getPlayerVoteChoice(nameDirectory)
        pm.setComponent(pId, Vote.name, Vote(target))
