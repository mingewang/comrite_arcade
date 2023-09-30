def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Test the function
n = 40  # You can change this value to calculate the Fibonacci number for a different n
result = fibonacci_recursive(n)
print(f"The Fibonacci number recusive for n = {n} is {result}")


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev, current = 0, 1
    for _ in range(2, n + 1):
        prev, current = current, prev + current

    return current

# Test the function
n = 100  # You can change this value to calculate the Fibonacci number for a different n
result = fibonacci(n)
print(f"The Fibonacci number for n = {n} is {result}")