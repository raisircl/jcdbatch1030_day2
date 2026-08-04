def iseven(num):
    """Check if a number is even."""
    return num % 2 == 0

evens=filter(iseven, [1, 2, 3, 14, 5, 16, 72, 83, 91, 10])
for e in evens:
    print(e)