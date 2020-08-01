import numpy as np

def square(x):
    """
    Raises a number to the second power.

    Parameters:
    x: The number

    Returns:
    The square of the number. Does not check for overflow
    """
    print("before recursion call")
    x = 2 * x
    if x >= 256:
        return
    square(x)
    print("after recursion call")

print(square(4))