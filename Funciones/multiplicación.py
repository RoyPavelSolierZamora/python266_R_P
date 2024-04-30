#
numero = float(input("Introduce un numero: "))
numero2 = float(input("Introduce otro numero: "))

def mult(num1, num2):
    print(f" La multiplicación es: {num1 * num2}")
    print(f"Estoy multiplicando la función {num1} y {num2}")
    
mult(numero, numero2)

mult(5,5)

#Saber como sacra valores del contexto local al contexto  global
numero = float(input("Introduce un numero: "))
numero2 = float(input("Introduce otro numero: "))

def mult(num1, num2):
    total =num1 * num2
    print(f"La multiplicación es: {total}")
    print("Estoy imprimiendo desde una función")
    return total

resultado = mult(5,5)
print(f"Este es el total fuera de la función: {resultado}")

#Otra forma, no lo hagan nunca, es malo
def mult(num1, num2):
    global total
    total =num1 * num2
    print(f"La multiplicación es: {total}")
    print("Estoy imprimiendo desde una función")
    return total

resultado = mult(5,5)
print(f"Este es el total fuera de la función: {resultado}")