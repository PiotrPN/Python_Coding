#infinite prime numbers
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

n=1
while True:
    for elem in range(n-1,n):  #loop with changing range iteration
        if is_prime(elem) is True:
            print(elem)
        n+=1

