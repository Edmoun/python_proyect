"""
Ejercicio: Si el usuario introduce un numero, si no es un numero indicar que debe
 de introducir un numero. Si es un numero, deberemos de comprobar si es o no par y notificarselo.

"""

num = input("Introduce un numero: ")
num = int(num)
if(type(num) == int):
    if(num % 2 == 0):
        print("Felicidades el numero es par")
    else:
        print("Felicidades igualmente, el numero es impar")
else:
    print("Introduce un numero entero cara de ñema")