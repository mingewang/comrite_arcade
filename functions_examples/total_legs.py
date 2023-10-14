'''
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species.
You have to implement a function that returns the total number of legs of all the animals.
'''

def total_legs(chickens: int, pigs:int, cows:int) -> int:
    return chickens *2 + pigs * 4 + cows * 4

user_input = input("please input chickens, pigs, cows: ")

chickens, pigs, cows = user_input.split()
print("your chickens: ", chickens)
print("your pigs: ", pigs)
print("your cows: ", cows)
total = total_legs(int(chickens), int(pigs), int(cows))

print("total legs is: ", total)
