from util import getInputInSeq

def _buildPromptString(nameItems):

    promptString = "Choose a player to target, or go back\n"
    for pId, name in nameItems:
        promptString += "  - {}\n".format(name)
    promptString += "  - Back\n"
    promptString += "\n>  "
    return promptString


# Prompts the user for whatever inputs are required to properly
# adjust game-state for the vote action.
# @param pId - The Player Id number for the current player
# @param pm  - The PlayerManager object for the game
# @return (True|False) - False indicates the user wishes to do some
#                        other action.
def userPrompt(pId, pm):
    nameDirectory = pm.getComponentDirectory('name')
    nameItems     = list(nameDirectory.items())
    promptString  = _buildPromptString(nameItems)

    print("You have chosen the 'Vote' action:\n")

    nameItems.append((-1, "back"))
    choice = getInputInSeq(promptString, [x[1] for x in nameItems])

    if nameItems[choice][0] == -1:
        return False

    targetPId = nameItems[choice][0]
    pm.setComponent(pId, 'vote', targetPId)
    return True
