# Apartado 1: Repaso de conceptos basicos.
numero = [1, 2, 3, 4, 5]
print(numero)

primerValor = numero[0]
print(primerValor)

longitud = len(numero)
print(f"El primer valor es: {primerValor}\nLa logitud de la lista es: {longitud}")

for num in numero:
    print(num)

# Apartado 2: Indexado y sublistas.
lista = ["Edmoun", "Ana", "Pedro", "Pacalito"]
print(lista)

ultimoElemnto = lista[-1]
print(ultimoElemnto)

anteUltimo = lista[-3]
print(anteUltimo)

sublista = lista[:3]
print(sublista)

sublista = lista[-3:-1]


# Apartado 3: Comprobar si una lista contiene o no un elemento.

listado = [1, 2, 3, 4, 5]
num1 = 1
num2 = 6

if num1 in listado:
    print("El numero esta en la lista")
if num2 not in listado:
    print("El numero no esta en la lista")

# Modificar elementos en una lista.

carros = ["Ford", "Lexus", "Chevrolet", "Suzuki"]
print(carros)

carros[2] = "Toyota"
print(carros)

carros[0] = carros[0] + "Car"
print(carros)

carros[2:4] = "Cara", "Culo"
print(carros)

carros[3:4] = "Yo", "Te quiero"
print(carros)

