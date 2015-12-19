class PlayerType:
    name = "PlayerType"

    def __init__(self, typeName):
        self.typeName = typeName

    def getPlayerName(self):
        return self.typeName

    def __str__(self):
        return self.typeName

class PlayerName:
    name = "PlayerName"

    def __init__(self, name):
        self.playerName = name

    def getPlayerName(self):
        return self.playerName

    def __str__(self):
        return self.playerName
