"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import sqrt

def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2
    return True

def smallest_multiply (numbers):
    numb = 1
    for n in range(2, numbers+1):
        power = 1
        if is_prime(n) is True:

            while n ** power < numbers:
                power += 1
            numb *= (n ** (power - 1))
    return numb
