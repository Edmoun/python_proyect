# Definicion de una funcion

def saludar():
    print("Hola Edmon, como estas brou")

saludar()
saludar()

# Funciones con argumentos

def saludar2(nombre):
    print("Hola " + nombre + "¿Como estas?")

saludar2("Edmoun")

# Funciones con retorno

def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

valor = sumar(20, 39)
print(valor)
#Otra forma de hacerlo
def sumar(num1, num2):
    return num1 + num2

valor = sumar(20, 39)
print(valor)

# Funciones con retorno( Toda funcion creada para retornar comparaciones daran como resultado valores booleano)

def sumar2(a, b):
    return a == b

resultado = sumar2(1, 1)
print(resultado)

if(resultado):
    print("Eso es verdad compa")
else:
    print("Eso es mentira loco")

resultado = sumar2(1, 2)
print(resultado)

resultado = sumar2(1, "1")
print(resultado)

# Funciones con argumentos con valor por defecto

def saludarPorDefecto(nombre = "Edmoun"):
    print("Hola " + nombre + ", cara de culo")

saludarPorDefecto()
saludarPorDefecto("Pedro")

# Funciones que retornan varios valores

def sumaYResta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

result1, result2 = sumaYResta(45, 23)
print("Los resultados son:\nSuma: " + str(result1) + "\nResta: " + str(result2))


