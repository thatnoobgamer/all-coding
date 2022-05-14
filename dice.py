import random
def dice():
    print("The dice rolled "+str(random.randrange(1,6)))
    repeat = input("Do you want to roll again? ")
    repeatlower = repeat.lower()
    try:
        if repeatlower == "yes":
            dice()

        if repeatlower == "no":
            SystemExit()

        else:
            raise SystemError()

    except:
        print("\nPlease enter yes or no after this rolls again.\n")
        dice()

dice()
