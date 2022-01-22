def mid_val(lower:float, upper:float) -> float:
    '''
        Essentially finding the mean, but since it's the boundaries of a continuous
        interval, we don't need to (and can't really without calculus) sum the intermediary 
        values, but 
    '''
    return (lower + upper) / 2

# Simple test to show that mid_val is equivalent to mean:
# mean = lambda numbers: sum(numbers) / len(numbers) # `numbers` is a list of values
# for m in range(10, 20):
#     print(mid_val(m, m+10) == mean(range(m, m+11))) # True, True, ..., True

int_f = lambda x: int(x)
float_f = lambda x: float(x)

def play_game(attempts_allowed:int, precision:int, lower, upper, val_type) -> dict:
    attempts_remaining = attempts_allowed
    game_results = ('won', 'attempts_taken', 'secret_number')
    while attempts_remaining > 0:
        attempts_remaining -= 1
        guess = round(val_type(mid_val(lower, upper)), precision)

        # We can set these at the top of the loop, since they'll be used >1 time
        result = input(f'My guess is {guess}. Is that [h]igh, [l]ow, or [c]orrect? ')
        attempts_taken = attempts_allowed - attempts_remaining
        # try_conj = "try" if attempts_taken == 1 else "tries"

        while result not in 'hlc':
            result = input("Your response must be either 'h' (high), 'l' (low), or 'c' (correct). Please try again: ")

        if result == "c":
            return dict(zip(game_results, (True, attempts_taken, guess)))
        if result == "h":
            upper = guess
        if result == "l":
            lower = guess
    return attempts_taken

def main():
    while True:
        print("Pick a number, and I'll try to guess it!")
        game_choice = input("Do you wish to play with [i]ntegers or [d]ecimal numbers? ")
        if game_choice == "i":
            print("\nGreat! Your number and boundaries must be integer values. If you enter a number with a decimal, it will be rounded down to the nearest integer.")
            print("\nFirst, choose your lower and upper bounds.")
            lower = int(input("What is the lower bound? "))
            upper = int(input("And what is the upper bound? "))
            while lower >= upper:
                print("Lower bound must be less than upper bound. Try again.")
                lower = int(input("Choose a lower bound: "))
                upper = int(input("Choose an upper bound: "))
            attempts_allowed = int(input("Finally, how many guesses am I allowed? "))
            print("\nLet's get to it!")

            game_result = play_game(attempts_allowed, 0, lower, upper, int_f)

        if game_choice == "d":
            precision = int(input("How many decimal places would you like me to use in my guesses? "))
            print(f'\nGreat! Your number may have *at most* {precision} decimal places. If your number has more than {precision} decimal places, it will be rounded to {precision} decimal places.')
            print(f'\nFirst, choose your lower and upper bounds. (They\'ll also be rounded to {precision} decimal places.)')
            lower = round(float(input("What is the lower bound? ")), precision)
            upper = round(float(input("And what is the upper bound? ")), precision)
            while lower >= upper: # Validation
                print("Lower bound must be less than upper bound. Try again.")
                lower = round(float(input("Choose a lower bound: ")), precision)
                upper = round(float(input("Choose an upper bound: ")), precision)
            attempts_allowed = int(input("Finally, how many guesses am I allowed? "))
            print("\nLet's get to it!")
        
            game_result = play_game(attempts_allowed, precision, lower, upper, float_f)

        if game_result.get('won'):
            print(f"Got it! I guessed that your number was {game_result['secret_number']} in {game_result['attempts_taken']} tries. Thanks for playing!")
        else:
            print(f"I failed! Even with {game_result['attempts_taken']} tries, I still failed to guess your number!")

        play_again = input("Would you like to play again? [y/N]: ")
        if not play_again or play_again not in "Yyes": break

if __name__ == '__main__':
    main()
