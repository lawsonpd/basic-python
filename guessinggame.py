import random

a=random.randint(1,10)

while True:
    b = int(input("Enter a number between 1 and 10: "))
    if a==b:
        print("Correct")
        quit()
    if a<b:
        print("Lower")
    if a>b:
        print("Higher")




