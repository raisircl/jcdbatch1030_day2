def sum(n1:int, n2:int) -> int:
    """Returns the sum of two numbers."""
    return n1 + n2

def biggest(n1:int, n2:int) -> int:
    """Returns the biggest of two numbers."""
    return n1 if n1 > n2 else n2

def table(n:int) -> list:
    """Returns the multiplication table of a number."""
    return [f"{n} * {i} = {n * i}" for i in range(1, 11)]