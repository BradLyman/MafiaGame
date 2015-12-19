class PlayerManager:
    def __init__(self):
        self.nextPId    = 0
        self.playerIds  = []
        self.components = {}

    def createPlayer(self):
        pId = self.nextPId
        self.nextPId += 1
        return pId

    def playerHasComponent(self, pId, compName):
        if compName not in self.components:
            return False
        if pId not in self.components[compName]:
            return False
        return True

    def setComponent(self, pId, compName, value):
        if compName not in self.components:
            self.components[compName] = {}
        self.components[compName][pId] = value

    def getComponent(self, pId, compName):
        return self.components[compName][pId]

    def getPlayersWithComponent(self, compName):
        return self.component[compName]
