#!/usr/bin/python3

"""This module contains a function that determines the winner of a prime
   number selection game
"""


def isWinner(x, nums):
    '''function determines the winner
    '''
    def is_prime(num):
        '''function for determining if a number is prime'''
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        '''function to select the prime numbers from 2 to n'''
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        '''the function for determinig the game structure'''
        primes = get_primes_up_to_n(n)
        return "Maria" if len(primes) % 2 == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if x < 1:
        return None
    elif nums is None:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
