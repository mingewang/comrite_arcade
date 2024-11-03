def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
n = int(input("Enter a number: "))
print(f"{n}! = {factorial_recursive(n)}")


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
n = int(input("Enter a number: "))
print(f"{n}! = {factorial_iterative(n)}")


import math
# Example usage
n = int(input("Enter a number: "))
print(f"{n}! = {math.factorial(n)}")