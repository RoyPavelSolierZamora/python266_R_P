manzanas = float(input("Ingresa cuantas manzanas vas a vender: "))
precio = float(input("Ingresa el precio de las manzanas: "))
descuento = 0.1
new_descuento = 0.15

print("Bienvenido al supermercado new")
print("La cantidad de manzanas es: ", manzanas)
print("El precio por unidad de manzanas es: ", precio)

if manzanas ==18:
    e_total = (manzanas*precio) - (manzanas*precio)*new_descuento
    print("Obtuviste un descuento especial, el monto total sería: ", e_total)
elif manzanas >=10:
    total = (manzanas*precio) - (manzanas*precio)*descuento
    print("Tiene un descuento de 10%, el total a pagar es: ", total)
else :
    n_total = manzanas*precio
    print("El monto a pagar es: ", n_total)

print("Gracias por su preferencia, vuelva pronto")