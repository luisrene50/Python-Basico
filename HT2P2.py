n = int(input("Introduce un número entero positivo: "))
p = 2
while n % p != 0:
    p += 1
if p == n:
    print(str(n) + " es un número primo")
else:
    print(str(n) + " no es un número primo")