from nightPhase import *
from gameInitialization import *
import Globals




(teams, players) = startGame()
for player in players:
	(targets, action, priority) = promptPlayerForAction(player, players)