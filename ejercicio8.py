#Ejercicio 4.6.1. Escribir funciones que resuelvan los siguientes problemas:

#Dado un número entero n, indicar si es o no par.
def isPar():
    num = int(input("Escribe un numero: "))
    if num % 2 == 0:
        print("El numero introducido es par")
    else:
        print("El numero introducido es impar")


#Dado un número entero n, indicar si es o no primo.

def isPrime(num):
    for n in range(2, num//2):
        if num % n == 0:
            return  False
    return True

print(isPrime(6))
