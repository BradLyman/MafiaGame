def process(pm):
    results       = {}
    voteDirectory = pm.getComponentDirectory('vote')

    for pId, targetPid in voteDirectory.items():
        if targetPid in results:
            results[targetPid] += 1
        else:
            results[targetPid] = 1

    # note -- ambiguous result in case of tie
    toKillPId  = max(results, key=(lambda key: results[key]))
    toKillName = pm.getComponent(toKillPId, 'name')

    pm.removePlayer(toKillPId)
    print("Votes are in! {} was lynched.".format(toKillName))
