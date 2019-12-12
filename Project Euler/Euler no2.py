"""project euler Problem 2
sum of even fibonacci elements"""
def fibonacci_evens_sum(range=4000000):
    fib_two_last=[1,2]
    even_sum=2
    while fib_two_last[1]<=range:
        numb=fib_two_last[0]+fib_two_last[1]
        if numb%2==0:
            even_sum+=numb
        fib_two_last.append(numb)
        fib_two_last.remove(fib_two_last[0])
    return even_sum

print(fibonacci_evens_sum())