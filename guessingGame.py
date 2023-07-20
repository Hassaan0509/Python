import random

key = random.randint(1, 100)
count = 0
print("Guess a number between 1 and 100")
guess = int(input("Enter your guess: "))
while guess != key:
    if key > guess:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input("Enter your guess: "))
    count += 1
print("You guessed it in", count, "tries")
