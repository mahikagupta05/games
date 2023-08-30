import random

num = random.randint(1,10)

guess = 0

while guess != num:
    guess = int(input("Guess a random number 1-10: "))
    if guess > num:
        print("Guess again, too high.")
    elif guess < num:
        print("Guess again, too low.")
print("You have guessed the random number!")
