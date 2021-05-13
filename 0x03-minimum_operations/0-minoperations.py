#!/usr/bin/python3
"""Interview preparation
    """


def minOperations(n):
    """text editor can execute only two operations in this file:
    Copy All and Paste.
    Args:
        n (int): write a method that calculates the fewest number
    Returns:
        int:  number of operations needed to result in exactly
    """

    quaOpperations = 0
    module = 2

    if n <= 1:
        return 0

    while n > 1:
        if n % module == 0:
            n = n / module
            quaOpperations = quaOpperations + module
        else:
            module += 1
    return quaOpperations
