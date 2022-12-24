"""Ejercicio 1.10.5. Escribir un programa que pregunte al usuario:

su nombre, y luego lo salude.
dos números y luego muestre el producto."""

def saludar():
    name = input("Escribe tu nombre: ")
    name = str(name)

    if type(name) == str:
        print(f"hola {name}")
    else:
        print("Escribe un nombre")

def producto():
    num1 = int(input("Escribre tu primer numero: "))
    num2 = int(input("Escribre tu segundo numero: "))

    print(num1*num2)

saludar(),producto()

