#Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.

# Solicitar al usuario que ingrese tres números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

# Verificar si los tres números son iguales
if numero1 == numero2 == numero3:
    print("Los tres números ingresados son iguales.")
elif numero1 == numero2 or numero2 == numero3 or numero1 == numero3:
    print("Los dos números ingresados son iguales.")
else :
    print("Los tres números son diferentes")