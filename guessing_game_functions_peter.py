# Guessing game functions

def game_decimals(precision:int):
    while True: # Game loop; break when user no longer wants to play.
        print(f'Your number may have *at most* {precision} decimal places. If your number has more than {precision} decimal places, it will be rounded to {precision} decimal places.')
        print(f'\nFirst, choose your lower and upper bounds. (They\'ll also be rounded to {precision} decimal places.)')
        lower = round(float(input("What is the lower bound? "), precision))
        upper = round(float(input("And what is the upper bound? ")), precision)
        while lower >= upper:
            print("Lower bound must be less than upper bound. Try again.")
            lower = round(float(input("Choose a lower bound: ")), precision)
            upper = round(float(input("Choose an upper bound: ")), precision)
        attempts_allowed = int(input("Finally, how many guesses am I allowed? "))
        print("\nLet's get to it!")

        for guess_attempt in range(attempts_allowed): # Turn into recursive function that takes `lower`, `upper`, and `attempts_allowed`?
            guess = round(mid_val(lower, upper), precision)
            result = input(f'My guess is {guess}. Is that [h]igh, [l]ow, or [c]orrect? ')

            while result not in 'hlc':
                result = input("Your response must be either 'h' (high), 'l' (low), or 'c' (correct). Please try again: ")

            if result == "c":
                try_conj = "try" if guess_attempt == 0 else "tries"
                print(f'Got it! I guessed your number in {guess_attempt + 1} {try_conj}. Thanks for playing!')
                break
            if result == "h":
                upper = guess
            if result == "l":
                lower = guess

        print(f'\nDarn! I guessed {attempts_allowed} times and still didn\'t find your number!')

def game_integers():
    while True: # Game loop; break when user no longer wants to play.
        print("Your number and boundaries must be integer values. If you enter a number with a decimal, it will be rounded down to the nearest integer.")
        print("\nFirst, choose your lower and upper bounds.")
        lower = int(input("What is the lower bound? "))
        upper = int(input("And what is the upper bound? "))
        while lower >= upper:
            print("Lower bound must be less than upper bound. Try again.")
            lower = int(input("Choose a lower bound: "))
            upper = int(input("Choose an upper bound: "))
        attempts_allowed = int(input("Finally, how many guesses am I allowed? "))
        print("\nLet's get to it!")

        for guess_attempt in range(attempts_allowed): # Turn into recursive function that takes `lower`, `upper`, and `attempts_allowed`?
            guess = round(int(mid_val(lower, upper)))
            result = input(f'My guess is {guess}. Is that [h]igh, [l]ow, or [c]orrect? ')
            
            while result not in 'hlc':
                result = input("Your response must be either 'h' (high), 'l' (low), or 'c' (correct). Please try again: ")
            
            if result == "c":
                try_conj = "try" if guess_attempt == 0 else "tries"
                print(f'Got it! I guessed your number in {guess_attempt + 1} {try_conj}. Thanks for playing!')
                break
            if result == "h":
                upper = guess
            if result == "l":
                lower = guess

        print(f'\nDarn! I guessed {attempts_allowed} times and still didn\'t find your number!')

# from typing import List
# Huge bug: actual (i.e., original) index is lost in recursive calls. Could try passing as kwarg.
# def binary_search(n:int, items:list) -> int:
#     i = math.floor(len(items) / 2) # index of middle element
#     current_item = items[i] # middle item
#     print(f'Index: {i}, current item: {current_item}')
#     if current_item == n:
#         return i
#     elif current_item < n:
#         return binary_search(n, items[i+1:])
#     elif current_item > n:
#         return binary_search(n, items[:i])
#     else:
#         return None
