import PlayerManager

pm = PlayerManager.PlayerManager();

p1 = pm.createPlayer();

print(pm.playerHasComponent(p1, "name"))

pm.setComponent(p1, "name", "fred");

print(pm.playerHasComponent(p1, "name"))
print(pm.getComponent(p1, "name"))
