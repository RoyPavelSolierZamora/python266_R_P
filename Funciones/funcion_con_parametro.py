#
name = "Roy" #contexto global

def saludo(nameFuncion):  #Contexto local
    name = "sochi"
    print(nameFuncion)
    print("Buen día")
    print(name)
    print("Buen día")
    print("===========")
    
saludo(name)
saludo("Felipe")

#
name = "Roy" #contexto global
idioma ='español'

def saludo(nameFuncion,idioma):  #Contexto local
    #name = "sochi"
    print(nameFuncion)
    print(f"Buen día en {idioma}")
   # print(name)
   # print("Buen día")
    print("===========")
    
saludo(name, idioma)
saludo(name, 'Aleman')
saludo("Felipe", 'Frances')

#
numero = float(int("Introduce un numero: "))
numero2 = float(int("Introduce otro numero: "))

def sum():
    print(numero + numero2)
    print(f"Estoy sumando la función {numero} y {numero2}")
    
sum




