import random
import time

a=random.randint(1,1000)
attemptnum = 1
oldb=101
print ("\n" * 2)
time.sleep(1)
print ("It's time to play a motherfucking game you fucking dildo.\n")
time.sleep(2)
print ("I'm thinking of a number from 1 to 1000.")
time.sleep(2)
print ("You have 10 guesses to get it right.\n")
time.sleep(2)
print ("If you fail, then you're one fine dumbass.\n")
time.sleep(2)

while (attemptnum < 12):

    if attemptnum==11:
        time.sleep(1)
        print("You had 10 guesses and now you have none. The number was",a,". Get fucked.\n")
        time.sleep(1)
        quit()

    b = int(input("Enter a number between 1 and 1000: "))
    time.sleep(0.5)
    print ("Thinking...")
    time.sleep(2)

    if b==oldb:
        print("You just typed that number you absolute piece of shit.")
        time.sleep(1)
        print("Just for that you can sit here and wait 10 seconds before your next attempt.\n")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("6")
        time.sleep(1)
        print("7")
        time.sleep(1)
        print("8")
        time.sleep(1)
        print("9")
        time.sleep(1)
        print("10\n")
        time.sleep(1)
        print("Okay, time out is over.\n")
        time.sleep(0.5)

    elif a==b:
        print("Correct. It took you",attemptnum,"tries to get it right. Now fuck off.\n")  
        time.sleep(1)
        quit()

    elif a<b:
        print("Lower, you fucking idiot. You have",10-attemptnum,"attempts remaining.\n")
        time.sleep(0.5)

    elif a>b:
        print("Higher, you spineless ape. You have",10-attemptnum,"attempts remaining.\n")
        time.sleep(0.5)

    attemptnum = attemptnum + 1
    oldb = b
    time.sleep(1)
