from PlayerManager import PlayerManager
from Components import *
import logging as log
import random

# set logger level, this should realy be done at
# program start
log.basicConfig(level="DEBUG")

class Game:
    def __init__(self, playerCount):
        self.pm      = PlayerManager();
        self.players = [];
        for i in range(0,playerCount):
            self.players.append(
                self.createPlayer()
            )
        log.info(self.players)
        self.setupPlayerNames()

    def createPlayer(self):
        # TODO: make this choice less stupid
        creator = random.choice([
            self.createCitizen,
            self.createMafia
        ])
        return creator()

    def createCitizen(self):
        pId = self.pm.createPlayer()
        self.pm.setComponent(pId, PlayerType("Citizen"))
        return pId

    def createMafia(self):
        pId = self.pm.createPlayer()
        self.pm.setComponent(pId, PlayerType("Mafia"))
        return pId

    def setupPlayerNames(self):
        for pId in self.players:
            promptStr = (
                "Player {}, enter name:\n".format(pId) )
            name = input(promptStr)
            self.pm.setComponent(pId, PlayerName(name))
            summaryStr = (
                "Welcome {}, you are playing as a {}"
                .format(
                    self.pm.getComponent(pId, PlayerName),
                    self.pm.getComponent(pId, PlayerType)
                )
            )
            print(summaryStr)

playerCount = 0;
playerCount = int(input("How many players?\n"))

game = Game(playerCount)
