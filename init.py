from Player import *
import Globals

Globals.globalPlayerTraits = [{'name' : 'Larry'}, {'name' : 'Curly'}, {'name' : 'Moe'}]
Larry = Citizen('Larry')
Curly = Citizen('Curly')
Moe = Citizen('Moe')
Larry.traits['targets'] = [Moe]
Larry.currentAction = 0
