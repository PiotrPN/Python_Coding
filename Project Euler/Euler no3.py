#What is the largest prime factor of the number 600851475143 ?

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
n=3
while True:
    if 600851475143%n==0:
        if is_prime(600851475143/n):
            print("found largest prime factor")
            print(600851475143/n)
            break
    n+=2

