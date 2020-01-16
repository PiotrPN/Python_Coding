gen = (x ** 2 for x in range(10) if x % 2 == 0)
gen2 = (x ** 2 for x in range(10) if x % 2 == 0)

for i in gen:
    print (f"{i}   result from loop iteration")

print()

while True:
    print(f"{next(gen2)}  result from next func")