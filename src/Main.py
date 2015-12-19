from PlayerManager import *

class Name:
    typeName = "Name"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

pm = PlayerManager()

p1 = pm.createPlayer()

print(pm.hasComponent(p1, Name.typeName))
pm.setComponent(p1, Name.typeName, Name("fred"))

print(pm.getComponent(p1, Name.typeName))
