from PlayerManager import PlayerManager
from Components import *
import logging as log
import random
from util import getIntInput

# set logger level, this should realy be done at
# program start
log.basicConfig(level="DEBUG")

class GameInitializer:
    def __init__(self):
        self.pm      = PlayerManager()
        self.players = []
        self.initializePlayers()
        self.setupPlayerNames()

    def initializePlayers(self):
        playerCount = getIntInput(
            "How many players are there?\n",
            0, 100
        );
        for i in range(0,playerCount):
            self.players.append(
                self.createPlayer()
            )
        log.info(self.players)

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
        self.pm.setComponent(pId, DayActions(["Vote"]))
        return pId

    def createMafia(self):
        pId = self.pm.createPlayer()
        self.pm.setComponent(pId, PlayerType("Mafia"))
        self.pm.setComponent(pId, DayActions(["Vote"]))
        return pId

    def getPlayerManager(self):
        return self.pm
