import random

secret = random.randint(1, 99)
guess = 0
tries = 0
left = 0

#print (type(secret))
#print (type(guess))

print ("AHOY! I'm Demon of powers and I have a treasure!")
print (" If you want my treasure you have to guess the code, It is a number from 1 to 99. I will give you 6 tries. ")

while guess != secret and tries < 6:
    guess = int(input("Whats your guess? \n"))
    #print (type(secret))
    #print (type(guess))*/
    if guess < secret:
        print ("Too low")
    elif guess > secret:
        print ("Too high")
    tries = tries + 1
    left = tr
    print ("Its  your", tries, "try")
if guess == secret:
    print ("avast! You guess the correct code, you get the treasure")
else:
    print ("No more guesses! Better luck next time")
    print ("The secret number was", secret)
