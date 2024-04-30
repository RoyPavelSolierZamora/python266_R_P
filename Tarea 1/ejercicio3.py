#3.- Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. No considerar el caso en que ambos números son iguales.

#Solicitando al usuario que ingrese dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

#Mostrando cuál de los dos es menor
if numero1 < numero2:
    print(f"El primer número ingresado es menor: {numero1}")
elif numero2 < numero1:
    print(f"El segundo número ingresado es menor: {numero2}")
    
print("Concluido")