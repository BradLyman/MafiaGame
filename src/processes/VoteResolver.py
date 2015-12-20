from components.Vote import Vote

def process(pm):
    results       = {}
    voteDirectory = pm.getComponentDirectory(Vote.name)

    for pId, vote in voteDirectory.items():
        if vote.target in results:
            results[vote.target] += 1
        else:
            results[vote.target] = 1

    # note -- ambiguous result in case of tie
    toKillPId  = max(results, key=(lambda key: results[key]))
    toKillName = pm.getComponent(toKillPId, 'name')

    pm.removePlayer(toKillPId)
    print("Votes are in! {} was lynched.".format(toKillName))
