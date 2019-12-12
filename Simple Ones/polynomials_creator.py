def polynomials(*args):
    a=len(args)
    f=f"{args[0]}*x**({a-1})"
    if a<=1:
        return args[0]
    else:
        for n,i in zip(args[1:],range(2,a+1)):
            if a-i==0:
                f+=f"+{n}"
            else:
                f+=f"+({n})*x^{a-i}"
    return f
print(polynomials(2,3,4,5,6,1))

