print("Roy")
print("Buen día")

#Otra forma
def saludo():
    print("Roy")
    print("Buen día")
    
saludo()
saludo()
saludo()
saludo()

#Con variable  #mala práctica
name = "Roy" #contexto global

def saludo():  #Contexto local
    print(name)
    print("Buen día")
    
print(name)
saludo()

