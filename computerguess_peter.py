def play_game(attempts_allowed:int, lower, upper, val_type) -> dict:
    attempts_remaining = attempts_allowed
    precision = 0
    while attempts_remaining > 0:
        attempts_remaining -= 1
        guess = round(val_type((lower+upper)/2), precision)
        result = input(f'My guess is {guess}. Is that [h]igh, [l]ow, or [c]orrect? ')
        attempts_taken = attempts_allowed - attempts_remaining
        while result not in 'hlc': # Validation
            result = input("Your response must be either 'h' (high), 'l' (low), or 'c' (correct). Please try again: ")
        if result == "c":
            return dict(zip(('won', 'attempts_taken', 'secret_number'), (True, attempts_taken, guess)))
        if result == "h":
            upper = guess
        if result == "l":
            lower = guess
        print(f'lower: {lower}; upper: {upper}; u/l diff: {upper - lower}; precision: {precision}')
        if round(upper - lower, precision) <= eval(f'1e{precision}'):
            precision += 1
    return attempts_taken

def main():
    while True:
        print("Pick a number, and I'll try to guess it!")
        lower, upper = float(input("What is the lower bound? ")), float(input("And what is the upper bound? "))
        while lower >= upper: # Validation
            print("Lower bound must be less than upper bound. Try again.")
            lower, upper = float(input("Choose a lower bound: ")), float(input("Choose an upper bound: "))
        attempts_allowed = int(input("Finally, how many guesses am I allowed? "))
    
        game_result = play_game(attempts_allowed, lower, upper, float)

        if game_result.get('won'):
            print(f"Got it! I guessed that your number was {game_result['secret_number']} in {game_result['attempts_taken']} tries. Thanks for playing!")
        else:
            print(f"I failed! Even with {game_result['attempts_taken']} tries, I still failed to guess your number!")

        play_again = input("Would you like to play again? [y/N]: ")
        if not play_again or play_again not in "Yyes": break

if __name__ == '__main__':
    main()
