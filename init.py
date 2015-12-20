from Player import *
import Globals

Globals.globalPlayerTraits = [{'name' : 'Larry'}, {'name' : 'Curly'}, {'name' : 'Moe'}]
Larry = Citizen('Larry')
Curly = Mafian('Curly')
Moe = Mafian('Moe')
Larry.traits['targets'] = [Moe]
Larry.currentAction = 0
Curly.traits['targets'] = [Larry]
Curly.currentAction = 0
Moe.traits['targets'] = [Larry]
Moe.currentAction = 0