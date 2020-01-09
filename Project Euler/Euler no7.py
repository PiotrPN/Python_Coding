"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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

def n_prime_number(number):
    n=1
    numb=2
    while n!=number:
        numb+=1
        if is_prime(numb):
            n+=1
    return numb
print(n_prime_number(10001))