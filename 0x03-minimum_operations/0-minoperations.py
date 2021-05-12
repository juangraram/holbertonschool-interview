#!/usr/bin/python3

def minOperations(n):
    """[In a text file, there is a single character H. Your text editor can execute only two operations in this file:]
        Copy All and Paste.
    Args:
        n ([numbers]): [write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.]

    Returns:
        Returns an integer
    """

    number = n
    module = 2
    qoperation = 0

    if n <= 1:
        return 0

    while number > 1:
        if number % module == 0:
            number = number / module
            qoperation = qoperation + module
        else:
            module += 1
    return qoperation
