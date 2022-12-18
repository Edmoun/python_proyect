"""Ejercicio 4: Tenemos un texto dondde queremos encontrar palabras claves. Las palabras claves 
pueden ser hasta 5 y deberemos pedirselas al usuario y guardarlas en una lista.
Si el usuario quiere poner menos de 5 palabras clave, debera escribir "fin" para 
terminar de introducir datos. Si el usuario introduce numeros o nada, deberemos
eliminarlos de la lista ante de la busqueda."""

"""En otra lista, deberemos guardar el numero de veces que aparece cada palabra clave en nuestro texto.
Por ejemplo, si las palabras claves son ordenador y portatil y aparecen 5 y 7 veces respectivamente
nuestras listas deberan aparecer asi:

keywords = ["odenador", "portatil"]
ocurrencias = [5, 7]"""

texto = """Un texto es una composición de signos codificados en un sistema de escritura que 
forma una unidad de sentido. También es una composición de caracteres imprimibles generados 
por un algoritmo de cifrado que, aunque no tienen sentido para cualquier persona, sí puede 
ser descifrado por su destinatario original."""

palabrasClaves =[]
numeroPalabra = []

for x in range(5):
    clave = input("Escribe las palabras claves y fin para dejar de escribir: ")
    if clave == "Fin":
        break
    else:
        palabrasClaves.append(clave)

Espacio = 0
while(True):
    if Espacio >= len(palabrasClaves):
        break
    if palabrasClaves[Espacio] == '':
        palabrasClaves.pop(Espacio)
    elif palabrasClaves[Espacio].isnumeric():
        palabrasClaves.pop(Espacio)
    else:
        Espacio += 1

print (Espacio)
print(palabrasClaves)   

texto = texto.replace('.','').replace(',','').split()

for x in range(len(palabrasClaves)):
    numeroPalabra.append(0)

for palabra in texto:
    for clave in palabrasClaves:
        if clave == palabra:
            posicion = palabrasClaves.index(clave)
            numeroPalabra[posicion] += 1
            break
print(numeroPalabra)