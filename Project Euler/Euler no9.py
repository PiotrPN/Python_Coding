"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

result=0
for b in range(1000):
    a = 1
    for a in range(b):
        c = (a ** 2 + b ** 2) ** (1 / 2)
        if a+b+c==1000 and a<b<c:
            print(f"a:{a}   b:{b}   c:{int(c)}")
            result=a*b*int(c)
            break

print(result)





