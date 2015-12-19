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
