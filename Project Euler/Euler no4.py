"""project euler Problem 4
Find the largest palindrome made from the product of two 3-digit numbers."""
def numbers(min,max):
    for n in range (min,max):
        for m in range(min,max):
            numb=n*m
            yield numb

def biggest_palindrome(min_numb,max_numb):
    palindrome=0
    for numb in numbers(min_numb,max_numb):
        if str(numb)==str(numb)[::-1]:
            if numb>palindrome:
                palindrome=numb
    return palindrome
print(biggest_palindrome(100,1000))