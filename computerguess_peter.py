import math

from typing import List

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

def mid_val(lower:float, upper:float) -> float:
    '''
        Essentially finding'''
    return (lower + upper) / 2

# Simple test to show that mid_val is equivalent to mean:
# mean = lambda numbers: sum(numbers) / len(numbers) # `numbers` is a list of values
# for m in range(10, 20):
#     print(mid_val(m, m+10) == mean(range(m, m+11))) # True, True, ..., True

def main():
    while True: # Main loop; break when user no longer wants to play.
        print("Pick a number, and I'll try to guess it!")
        print("\nFirst, let's choose a lower and an upper bound.")
        lower = input("What is the lower bound? ")
        upper = input("And what is the upper bound? ")
        attempts_allowed = input("Finally, how many guesses am I allowed? ")
        print("\nLet's get to it!")

        for guess_attempt in range(attempts_allowed): # Turn into recursive function that takes `lower`, `upper`, and `attempts_allowed`?
            guess = mid_val()
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
        play_again = input("Would you like to play again? [y/N]: ")
        if play_again not in "Yyes": break

if __name__ == '__main__':
    main()
