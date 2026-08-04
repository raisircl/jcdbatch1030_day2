from functools import reduce
def multiply(x, y):
    """Multiply two numbers."""
    return x * y

fact=reduce(multiply, [1, 2, 3, 4, 5])
print(f"Factorial of 5 is: {fact}")
