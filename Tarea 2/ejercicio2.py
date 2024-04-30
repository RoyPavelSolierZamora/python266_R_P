# 2.- Escriba un algoritmo que lea del teclado un número entero y que compruebe si el número es menor que 10. 
# Si no lo está, debe volver a leer el número repitiendo la operación hasta que el usuario escriba un valor correcto. 
# Finalmente, debe escribir por pantalla el valor leído cuando este sea correcto.

#Inicializando una variable para almacenar el número ingresado
numero = None

#Creando el bucle para leer el número hasta que sea correcto
while True:
    try:
        numero = int(input("Ingrese un número entero: "))
        if numero < 10:
            break  #Salir del bucle si el número es menor que 10
        else:
            print("El número debe ser menor que 10. Intenta nuevamente.")
    except ValueError:
        print("Por favavor, ingresa un número entero válido.")

#Motrando el valor leído cunado es correcto
print(f"El número ingresado es: {numero}")