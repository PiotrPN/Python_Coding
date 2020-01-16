#Szyfr cezara
def crypt(tekst,numer):
    alfabet=[]
    for n in range (65, 91):
        alfabet.append(chr(n))
    wyraz=""

    for n in tekst:
        if n in alfabet:
            wyraz+=(alfabet[(numer+alfabet.index(n.upper()))%26])
        else:
            wyraz+=n
    return wyraz

def encrypt(tekst,numer):
    alfabet=[]
    for n in range (65, 91):
        alfabet.append(chr(n))
    wyraz=""

    for n in tekst:
        if n in alfabet:
            wyraz+=(alfabet[(-numer+alfabet.index(n.upper()))%26])
        else:
            wyraz+=n
    return wyraz
