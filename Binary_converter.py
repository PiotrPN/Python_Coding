"""Simply binary converter"""
def binary_to_numb(number):
    number =str(number)
    test=number[::-1]
    power=0
    result=0
    for n in test:
        if int(n)==1:
            result +=2**power
        power +=1
    return result

def numb_to_binary(number):
    tekst=""
    test=1
    power=0
    while test<=number:
        test*=2
        power+=1
    if number==0:
        tekst="0"
    else:
        for n in range(1,power+1):
            if number>=2**(power-n):
                tekst=tekst+"1"
                number=number-2**(power-n)
            else:
                tekst=tekst+"0"
    return tekst
