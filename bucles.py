# Introducion a las listas.

numeros = [1,2,3,4,5]

print(numeros[3])
print(numeros)
print(numeros[0])
print(len(numeros))

text = ["Edmoun", 3, "Ana"]
print(len(text) -1)

# Bucles For.

for x in range(5):
    print(x)
for c in range(1, 5):
    print(c)
for v in range(4, 20, 2):
    print(v)

# Ejemplo: Imprimir las vocales de una palabra.

palabra = "Pedro"

for letra in palabra:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)
    else:
        print("No es una vocal")
    
# Ejemplo: Iterar sobre una lista

numeros = [22, 33, 44, 55]
for numero in numeros:
    print(numero)
    numero += 10
    print(numero)
print(numeros)

num = [1, 2, 3, 4, 5]
for indice in range(len(num)):
    num[indice] += 10
print(num)


# Bucles While
contador = 0
while(contador < 10):
    print(contador)
    contador += 1

"""letra = "a"
frase = "Estoy con mi madre"
indice = 0
letraEncontrada = False

while(not(letraEncontrada)):
    if(frase[indice] == "a"):
        letraEncontrada = True
        print(f"Ya hemos encontrado la letra {letra} en la posicion {indice}")
    else:
        indice += 1"""

# Break
letra = "a"
frase = "Estoy con mi mamá"

for caracter in frase:
    if(caracter == letra):
        print(f"Haz encontrado la letra {letra} en la posicion {frase.index(letra)}")
        print(caracter)
        break
    else:
        print("Letra no encontrada")

# Continue

ltr = "e"
frs = "stoy con mi hermane"
sumador = 0

for carac in frs:
    if(carac == ltr):
        sumador += 1
        print(f"Letra encontrada {sumador} veces")
        continue

# Pass

lista = [0,1,2,3,45,50]
for num in lista:
    if(num == 1):
        pass
        print(f"El valor de jose es {num}")

# Else

frase = " Estoy aqui"
count = 0

for caracter in frase:
    count += 1


else:
    print(f"La cantidad de letras es {count}")