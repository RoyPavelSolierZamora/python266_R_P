numero = "10000014445,456,445,86,5,76"
print(numero.split(","))
for numero in numero.split(","):
    print(numero)
    
#Otra forma más mejor
numero = "10000014445,456,445,86,5,76"  #esto es una lista de textos
listaDeNumero = [10000014445,456,445,86,5,76] #esto es una lista de numeros

print(numero[0])
print(listaDeNumero[0])

print(len(listaDeNumero))  #hay 6 posiciones

#Para agregar números
calificacionesTallerPython= []
contador = 0

while contador <14:
    calificacion= float(input("Ingresa la primera calificacion: "))
    calificacionesTallerPython.append(calificacion)
    contador+=1
print(calificacionesTallerPython)

suma = 0
for calificacion in calificacionesTallerPython:
    suma = suma + calificacion

promedio = suma / len(calificacionesTallerPython)
print(promedio)