#!/usr/bin/python3

"""This module contains a function that determines the fewest number
   of coins needed to meet a given amount which is the total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    '''Initialize an array to store the minimum number of coin for each
       amount and also set the default value to be greater than any
       possible number of coins
    '''
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make change for 0
    dp[0] = 0

    # Iterate over each coin and update the minimum number of coins needed
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    '''If dp[total] is still the initial value,
       no combination of coins can make the total
    '''
    return dp[total] if dp[total] != float('inf') else -1
