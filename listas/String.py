nombre = "Oscar"
nombre =input("Ingresa tu nombre: ")

for letra in nombre:
    print(letra)

print(nombre.upper())  #Todo mayusculas
print(nombre.lower())  #Todo minuscula
print([0])
print([2])
print(nombre[::-1])  #imprimir alreves
print(nombre.replace('s','a')) #remplazar o quitar a la cadena esas letras
print(nombre.split("a")) #partir la letra espicífica
print(nombre[0:4])  #para extraer subcadena, para que muestre las primeras tres cadenas