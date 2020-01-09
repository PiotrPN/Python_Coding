"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
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
result=0

for numb in range(2*10**6):
    if is_prime(numb):
        result+=numb
    numb+=1
    if numb%100000==0:
        print(f"{numb/(2*10**6)*100}%")
print(result)
