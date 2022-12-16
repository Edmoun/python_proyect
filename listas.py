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

sublista = lista[0:3]
print(sublista)

sublista = lista[-3:-1]


# Apartado 3: Comprobar si una lista contiene o no un elemento.

# Modificar elementos en una lista.