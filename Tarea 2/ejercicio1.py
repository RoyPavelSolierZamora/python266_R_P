#1.- Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

# Inicializar la variable para almacenar la sumatoria
sumatoria = 0

# Bucle while para leer números enteros hasta que el usuario ingrese 0
while True:
    try:
        numero = int(input("Ingresa un número entero (0 para salir): "))
        if numero == 0:
            break  # Salir del bucle si se ingresa 0
        sumatoria += numero
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

# Mostrar la sumatoria de todos los números ingresados
print(f"La sumatoria de los números ingresados es: {sumatoria}")

