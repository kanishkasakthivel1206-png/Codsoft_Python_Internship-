# CodeSoft Python Programming Internship
# Task 4: Rock-Paper-Scissors Game

import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
draws = 0

print("=================================")
print("     ROCK PAPER SCISSORS GAME")
print("=================================")

while True:

    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter your choice: ").lower().strip()

    # Convert numbers into choices
    if user_choice == "1":
        user_choice = "rock"
    elif user_choice == "2":
        user_choice = "paper"
    elif user_choice == "3":
        user_choice = "scissors"

    # Check valid input
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    # Computer selects randomly
    computer_choice = random.choice(choices)

    print("\nYour choice     :", user_choice)
    print("Computer choice :", computer_choice)

    # Determine winner
    if user_choice == computer_choice:
        print("Result: It's a DRAW!")
        draws += 1

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: YOU WIN!")
        user_score += 1

    else:
        print("Result: COMPUTER WINS!")
        computer_score += 1

    # Display score
    print("\n----- SCORE -----")
    print("Your score     :", user_score)
    print("Computer score :", computer_score)
    print("Draws          :", draws)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        break

print("\n=================================")
print("           FINAL SCORE")
print("=================================")
print("Your score     :", user_score)
print("Computer score :", computer_score)
print("Draws          :", draws)

print("\nThank you for playing!")
