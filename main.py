import random
number = random.randint(1,  100)

guess = int(input("What number am I thinking of ?"))
while guess != number:

    if guess > number:
        print("Too high.")
        guess = int(input("What number am I thinking of ?"))

    elif guess < number:
        print("Too low.")
        guess = int(input("What number am I thinking of ?"))

print("You got it!")
