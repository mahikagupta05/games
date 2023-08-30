import random

user_choice = input("Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")

computer_choice = random.choice(['r', 'p', 's'])

# r > s, s > p , p > r
if user_choice == computer_choice:
    print("You tied.")
elif user_choice == 'r' and computer_choice == 's':
    print("You win! You beat scissors with rock.")
elif user_choice == 's' and computer_choice == 'p':
    print("You win! You beat paper with scissors.")
elif user_choice == 'p' and computer_choice == 'r':
    print("You win! You beat rock with paper.")
else:
    print("Aww, you lose!")
    

