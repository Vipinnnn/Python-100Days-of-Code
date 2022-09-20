import random

users_choice = int(
    input("Enter your choice, 0 for Rock 1 for Paper 2 for Scissors: "))


choices = ["Rock", "Paper", "Scissor"]
computers_choice = random.choice(choices)

if choices[users_choice] == "Rock" and computers_choice == "Paper":
    print(
        f"Your choice is: {choices[users_choice]} & computer's choice is: {computers_choice}, {computers_choice} wins!")
elif choices[users_choice] == "Rock" and computers_choice == "Scissor":
    print(
        f"Your choice is: {choices[users_choice]} & computer's choice is: {computers_choice}, {choices[users_choice]} wins!")
elif choices[users_choice] == "Paper" and computers_choice == "Scissor":
    print(
        f"Your choice is: {choices[users_choice]} & computer's choice is: {computers_choice}, {computers_choice} wins!")
elif choices[users_choice] == "Paper" and computers_choice == "Rock":
    print(
        f"Your choice is: {choices[users_choice]} & computer's choice is: {computers_choice}, {choices[users_choice]} wins!")
elif choices[users_choice] == "Scissor" and computers_choice == "Rock":
    print(
        f"Your choice is: {choices[users_choice]} & computer's choice is: {computers_choice}, {computers_choice} wins!")
elif choices[users_choice] == "Scissor" and computers_choice == "Rock":
    print(
        f"Your choice is: {choices[users_choice]} & computer's choice is: {computers_choice}, {computers_choice} wins!")
else:
    print(
        f"Your choice is: {choices[users_choice]} & computer's choice is: {computers_choice}, It's a tie.")
