import random

choice_1 = "rock"
choice_2 = "paper"
choice_3 = "scissors"


while True:
    player_choice = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    
    if player_choice == 'quit':
        print("Goodbye!")
        break
    
    if player_choice != choice_1 and player_choice != choice_2 and player_choice != choice_3:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # inclusive
    computer_choice_number = random.randint(1,3)
    if computer_choice_number == 1 :
        computer_choice = choice_1
    elif computer_choice_number == 2 :
        computer_choice = choice_2
    else:
        computer_choice = choice_3

    print(f"Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")