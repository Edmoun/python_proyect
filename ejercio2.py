"""
Ejercicio 1: Funcion maximo, dado dos numeros, la funcion debe de encontrar cual de los dos es el
mas grande y retornarlo. Extra: se deben comprobar que los argumentos de la funcion sean tipo int 
o float. Si alguno de los dos no lo es mostrar un error y retornar falso
"""

def mayor(a, b):
    if((type(a) == int or type(a) == float and type(b) == int or type(b) == float)):

        if(a > b):
            return a
        elif(a == b):
            print("son iguales")
        else:
            return b
    else:
        print("Error, no cumple los requisitos")
result = mayor(4, 3)
print("El mayor es: " + str(result))


"""
Ejercicio 2: Mini calculadora. Pedirle al usuario una operacion y dos numeros. Las operaciones
pueden ser suma, resta, potencia, etc. Si introduce una operacion diferente a estas mostrar un
mensaje de error. Si la operacion esta incluida mostrar el resultado.
"""

def miniCalculadora():
    operacion = input("Escribe una operacion: ")
    num1 = float(input("Escribe un numero: "))
    num2 = float(input("Escribe un numero: "))
    
    if(operacion == "suma"):
        print(num1+num2)
    elif(operacion == "resta"):
        print(num1-num2)
    elif(operacion == "multiplicacion"):
        print(num1*num2)
    elif(operacion == "division"):
        print(num1/num2)
    else:
        print("Error, introduce una operacion")
    
miniCalculadora()
    

