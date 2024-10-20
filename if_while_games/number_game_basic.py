
import random


random.randint(0, 100)


random_number = 23
print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100. ")

while True:
    guess = int(input("Enter your guess: "))
    if guess < random_number:
        print("Too low! Try a higher number.")
    elif guess > random_number:
        print("Too high! Try a lower number.")
    else:
        break

print("Congratulations! ")