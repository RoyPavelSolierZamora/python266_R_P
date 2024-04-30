#4.- Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400

# Solicitar al usuario que ingrese un año
anio = int(input("Ingresa un año: "))

# Verificar si el año es bisiesto
if anio % 4 == 0:  #Esta línea verifica si el año ingresado es divisible por 4. El operador % devuelve el residuo de la división del año entre 4. Si el residuo es 0, significa que el año es divisible por 4.
    if anio % 100 != 0 or anio % 400 == 0:  #Si el año es divisible por 4, entonces se verifica si el año no es divisible por 100 o si es divisible por 400. Esto se debe a que un año es bisiesto si es divisible por 4, pero no es bisiesto si es divisible por 100, a menos que también sea divisible por 400.
        print(f"El año {anio} es bisiesto.")
    else:
        print(f"El año {anio} no es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")