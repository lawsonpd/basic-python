playagain="y"
userchoice="y"
b="whatever"

while playagain==userchoice:

    print("\nI'll try to guess the number you're thinking of.")

    minnum = int(input("What is the lower bound? "))
    maxnum = int(input("What is the upper bound? "))
    numtries = int(input("How many guesses should I get? "))

    attempts = 0
    playagain="y"
    userchoice="y"

    while (attempts != numtries) & ((b == "c") == False):

        guess=int(((maxnum-minnum)/2)+minnum)

        attempts = attempts + 1

        print("\nThis is attempt number", attempts, "out of", numtries)
        print("My guess is", guess)
        b = input("Is that [c]orrect, [h]igh, or [l]ow? ")

        if b=="h":
            maxnum = (guess-1)

        if b=="l":
            minnum = (guess+1)

        if b=="c":
            print("\nI guessed your number! It was", guess)
            print("It took me",attempts,"tries to get it right.")

    if attempts > numtries:
        print("\nI ran out of guesses! Sorry.\n")

    userchoice = input("\nDo you want to play again? [y]es or [n]o? ")
    attempts=0
    b="whatever"

print ("\nThanks for playing! Goodbye.\n")


