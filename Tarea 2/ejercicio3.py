# 3.- Modifique el algoritmo del problema anterior para que, en vez de comprobar que el número sea menor que 10, 
# compruebe que se encuentre en el rango (0, 20).

#Inicializando una variable para almacenar el número ingresado
numero_ = None

#Creando el bucle para leer el número hasta que sea correcto
while True:
    try:
        numero_ = int(input("Ingrese un número entero: "))
        if 0 < numero_ < 20:
            break  #Salir del bucle si el número se encuentra entre 0 a 20
        else:
            print("El número debe ser menor que 20 y mayor que 0. Intenta nuevamente.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

#Motrando el valor leído cunado es correcto
print(f"El número ingresado es: {numero_}")