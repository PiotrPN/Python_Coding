"""project euler Problem 4
Find the largest palindrome made from the product of two 3-digit numbers."""
palindrome=set()
for n in range (100,1000):
    for m in range(100,1000):
        numb=str(n*m)
        if numb==numb[::-1]:
            palindrome.add(n*m)
print(max(palindrome))