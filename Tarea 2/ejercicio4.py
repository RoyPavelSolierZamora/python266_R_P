# 4.- Modifique el algoritmo del problema anterior para que cuente las veces que ha leído un número de teclado y 
# escriba el resultado por pantalla.

#Inicializando una variable para almacenar el número ingresado
numero_ = None
contador = 0

#Creando el bucle para leer el número hasta que sea correcto
while True:
    try:
        numero_ = int(input("Ingrese un número entero y cero para salir: "))
        if numero_ == 0:
            break  #Salir del bucle si el número se encuentra igual a 0
        elif 0 < numero_ < 20:
            contador += 1
        else:
            print("El número debe ser menor que 20 y mayor que 0. Intenta nuevamente.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

#Motrando el valor leído cunado es correcto
print(f"El número ingresado es: {numero_}")
print(f"Se leyeron {contador} números en total.")