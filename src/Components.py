class PlayerType:
    name = "PlayerType"

    def __init__(self, typeName):
        self.typeName = typeName

    def __str__(self):
        return self.typeName

class PlayerName:
    name = "PlayerName"

    def __init__(self, name):
        self.playerName = name

    def __str__(self):
        return self.playerName

class DayActions:
    name = "DayActions"

    def __init__(self, actionNames):
        self.actionNames = actionNames

    def __str__(self):
        return self.actionNames.__str__()
