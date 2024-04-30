# 2.- Solicitar al usuario un número de cliente. Si el número es el 1000, imprimir "Ganaste un premio".

#Dando bienvenida
print("Bienvenido")

#Solicitando el número de cliente
numero = float(input("Ingrese su número de cliente: "))

#Verificando el número ganador
if numero == 1000:
    print("Ganaste un premio")
else:
    print("Número verificado")