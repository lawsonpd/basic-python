while True:

    print("\nI'll try to guess the number you're thinking of.")

    min_num = int(input("What is the lower bound? "))
    max_num = int(input("What is the upper bound? "))

    # Validate input: min_num can't be greater than max_num
    while min_num > max_num:
        print("Lower bound must not be greater than the upper bound.\n")
        min_num, max_num = int(input("What is the lower bound? ")), int(input("What is the upper bound? "))

    num_tries = int(input("How many guesses should I get? "))

    # Validate input
    while num_tries < 1:
        num_tries = input("Number of guesses must be 1 or greater.\nPlease try again: ")

    print(f"Great! I have {num_tries} guesses. Let's go!")

    attempts_so_far = 0 # Number of guesses made

    while True:
        guess = int(((max_num - min_num) / 2) + min_num)

        if guess < min_num or guess > max_num:
            print("You tricked me!")
            break

        attempts_so_far += 1

        print("This is attempt number", attempts_so_far, "out of", num_tries)
        print("My guess is", guess)
        guess_result = input("Is that [c]orrect, [h]igh, or [l]ow? ")

        if guess_result == "h":
            max_num = guess - 1

        if guess_result == "l":
            min_num = guess + 1

        if guess_result == "c":
            print("\nI guessed your number! It was", guess)
            print("It took me", attempts_so_far, "tries to get it right.")
            break

        # Validate input
        else:
            while guess_result not in "hlc":
                guess_result = input("Please choose either [c]orrect, [h]igh, or [l]ow: ")

        if attempts_so_far >= num_tries:
            print("\nI ran out of guesses! Sorry.\n")
            break

    user_choice = input("\nDo you want to play again? [y]es or [n]o? ")
    
    if user_choice == "n": break

print ("\nThanks for playing! Goodbye.\n")
