"""project euler Problem 1
sum of the all mulfiplies of 3 and 5 less than 1000"""
def sum_of_multiplies(number):
    numbers=set()
    for n in range(number):
        if n%3==0 or n%5==0:
            numbers.add(n)
    return sum(numbers)
print(sum_of_multiplies(1000))