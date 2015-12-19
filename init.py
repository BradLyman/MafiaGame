from Player import *
from Globals import *
globalPlayerTraits = [{'name' : 'Larry'}, {'name' : 'Curly'}, {'name' : 'Moe'}]
Larry = Citizen('Larry')
Curly = Citizen('Curly')
Moe = Citizen('Moe')
Larry.traits['targets'] = [Moe]
Larry.currentAction = 0