import random
number = random.randint(1,  100)

guess = int(input("Quel est le nombre au quel je pense ?"))
while guess != number:

    if guess > number:
        print("Trop grand")
        guess = int(input("Quel est le nombre au quel je pense ?"))

    elif guess < number:
        print("Trop petit")
        guess = int(input("Quel est le nombre au quel je pense ?"))

print("Bravo !")
