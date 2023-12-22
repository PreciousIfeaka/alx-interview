#!/usr/bin/python3

"""This module contains a function that determines the fewest number
   of coins needed to meet a given amount which is the total
"""


def makeChange(coins, total):
    # Base cases
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Initialize the result to a large value
    result = float('inf')

    # Try using each coin and recursively calculate the number of coins needed
    for coin in coins:
        if coin <= total:
            subproblem_result = makeChange(coins, total - coin)
            if subproblem_result != -1:
                result = min(result, subproblem_result + 1)

    '''If result is still initialized to a large value, no
       combination of coins can make the total
    '''
    return result if result != float('inf') else -1
