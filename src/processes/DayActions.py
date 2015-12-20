import processes.actions.Directory as Dir

def process(pm):
    nameDirectory = pm.getComponentDirectory('name');

    # ask each player who they vote to lynch
    for pId, name in nameDirectory.items():
        Dir.actionDirectory['vote'](pId, pm)
