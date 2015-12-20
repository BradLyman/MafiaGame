def getIntInput(prompt, bot, top):
    result = 0
    while True:
        try:
            result = int(input(prompt))
            if result < bot or result > top:
                print("Oops! Number should be between {}, and {}".format(bot, top))
                continue
        except:
            print("Oops! I need a number.")
            continue
        else:
            return result

def getIntInputInSeq(prompt, seq):
    result = seq[0]
    while True:
        try:
            result = int(input(prompt))
            if result not in seq:
                print("Oops! Number should be one of {}".format(seq))
                continue
        except:
            print("Oops! I need a number")
        else:
            return result

