# Entrada de atos del usuario e identificacion de tipos de datos.

edad = input("Escribe tu edad por favor: ")
print(edad)

tipoDeDato = type(edad)
print(tipoDeDato)

# Booleans, if.

verdadero = True
falso = False

if(verdadero == True):
    print("Este casa bichos es un care de culo")

mayor = 5
menor = 3

if(mayor < menor):
    print("Soy mas fuerte que tu")

# Operadores de comparacion else, elif.

edad = input("Dime tu edad por favor: ")
edad = int(edad)
if(edad >= 18):
    print("Eres mayor, puedes pasar")
elif(edad < 0):
    print("Diablo pero que maldito jablador")
else:
    print("Vete de aqui bendito bicho culo cagao")


# Operadores logicos and, or, not.

edad = input("Dime tu edad por favor: ")
edad = int(edad)
if(type(edad) == int):
    if(edad > 120 or edad < 0):
        print("Eso no es posible")
    elif(edad > 18 and edad < 40):
        print("Estas admitido a mi club")
    else:
        print("Eres un mama bicho")
else:
    print("Hey compa tienes que decirme un numero entero")


#Funcion isnumeric.

texto = "Edmoun"
txt = "33"

print(texto.isnumeric())
print(txt.isnumeric())