#Sieve of Eratosthenes
def sieve(number):
    zbior1={n for n in range(2,number+1)}
    zbior2=set()
    for element in zbior1:
        for mnoznik in range(2,(number//element)+1):
            zbior2.add(element*mnoznik)
    result=list(zbior1-zbior2)
    result.sort()
    return result
print(sieve(5000))