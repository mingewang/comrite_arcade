import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Initialize variables
attempts = 0
max_attempts = 10
is_guess_correct = False

print("Welcome to the Number Guessing Game!")
print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")

while attempts < max_attempts:
    # Get the player's guess
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < random_number:
        print("Too low! Try a higher number.")
    elif guess > random_number:
        print("Too high! Try a lower number.")
    else:
        is_guess_correct = True
        break

if is_guess_correct:
    print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {random_number}.")

