#!/usr/bin/python3

def minOperations(n):
    """[In a text file, there is a single character H. Your text editor can execute only two operations in this file:]
        Copy All and Paste.
    Args:
        n ([numbers]): [write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.]

    Returns:
        Returns an integer
    """

    module = 2
    numOpperations = 0


    if n <= 1:
        return 0

    while n > 1:
        if n % module == 0:
            n = n / module
            numOpperations = numOpperations + module
        else:
            module += 1
    return numOpperations
