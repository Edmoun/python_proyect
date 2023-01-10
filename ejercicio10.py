"""Ejercicio 2.8.6. Escribir un programa que reciba un número n por parámetro 
e imprima los primeros n números triangulares, junto con su índice. 
Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n. 
Es decir, si se piden los primeros 5 números triangulares, el programa debe imprimir:"""

def numTriangular(n):
    if type(n) == int:
        print((n*n+n)//2)

print(numTriangular(3))