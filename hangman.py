import random

from words import words

chosen_word = random.choice(words)

#guess = input("Guess a letter a-z: ")


correct_letters = []
guessed_letters = []

def current_word():
    #first we print a list of all the correct letters the person has guessed so far
    if (guess in chosen_word) and (guess not in correct_letters):
        correct_letters.append(guess) #if u guessed l then correct_letters would be ['b', 'l']
    #then we want to print what the word looks like so far
    word_as_list = list(chosen_word) #['b', 'l', 'u', 'e']
    for letter in word_as_list:
        if letter not in correct_letters:
            word_as_list[chosen_word.rfind(letter)] = "-"
    print(f"Your word so far: {str(word_as_list)}")

errors = 0
for letter in guessed_letters:
    if letter not in word_as_list:
        errors += 1
        
while errors <= 10:
    guess = input("Guess a letter a-z: ")
    #correct guess 
    if guess in chosen_word:
        print(f"You guessed correctly! {guess} is the " + str(chosen_word.rfind(guess) + 1) + " letter." )
    #wrong guess
    if guess not in chosen_word:
        print("This letter is not in the word!")
    #printing what current word looks like
    current_word()
    #guessing the same letter more than once
    if guess in guessed_letters:
        print("You have already guessed this letter. Remember not to guess the same letter more than once.")
    #add guess to a list of guessed words
    if guess not in guessed_letters:
        guessed_letters.append(guess)
    print(f"These are the letters you have guessed so far: {str(guessed_letters)}")

#make upper and lower the same


        

    