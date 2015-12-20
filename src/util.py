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

# Prompt the user for a string in the sequence.
# Not case sensitive.
# @param prompt - String prompt to show the user
# @param seq    - Sequence (list, array, etc...) of valid response strings.
# @return (Int) Index of retrieved input
def getInputInSeq(prompt, seq):
    result    = ""
    allCapSeq = [x.upper() for x in seq]
    print(allCapSeq)
    while result not in allCapSeq:
        result = input(prompt).upper()
        if result not in allCapSeq:
            print("Oops! That doesn't seem to be valid input, try again.")

    return allCapSeq.index(result)
