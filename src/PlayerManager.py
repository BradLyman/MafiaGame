class PlayerManager:
    def __init__(self):
        self.nextPId    = 0
        self.playerIds  = []
        self.components = {}

    def createPlayer(self):
        pId = self.nextPId
        self.nextPId += 1
        return pId

    def playerHasComponent(self, pId, comp):
        compName = comp.name
        if compName not in self.components:
            return False
        if pId not in self.components[compName]:
            return False
        return True

    def setComponent(self, pId, comp):
        compName = comp.name
        if compName not in self.components:
            self.components[compName] = {}
        self.components[compName][pId] = comp

    def getComponent(self, pId, comp):
        compName = comp.name
        return self.components[compName][pId]

    def getPlayersWithComponent(self, comp):
        return self.component[comp.name]
