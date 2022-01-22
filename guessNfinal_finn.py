import math

lowerBound = float ( input('Enter lower inclusive bound:') ) - 1
upperBound = float ( input('Enter upper inclusive bound:') ) + 1

win = ''
numGuesses = 0

while not win in ['y', 'Y', 'yes', 'Yes']:
    floatDigits = max( int( - math.log10(upperBound - lowerBound) + 1.001) , 0) # what the fuck
    
    midpoint = (upperBound + lowerBound) / 2

    print('Debug: float, LB, MID, UB:', floatDigits, lowerBound, midpoint, upperBound)

    guess = round(midpoint, floatDigits)
    numGuesses += 1
    
    print('My guess number', numGuesses, ': \033[92m', guess, '\033[0m')
    win = input('[q] my guess is high. [z] my guess is low. Did I win? ')
    if win == 'q':
        upperBound = guess
    if win == 'z':
        lowerBound = guess
