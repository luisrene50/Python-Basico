name = input("¿Ingrese su nombre por favor? ")
genero = input("¿Es Hombre o mujer (H,M)? ")
if (genero == "M" and name.lower() < 'm') or (genero == "H" and name.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es " + grupo)