"""Ejercicio 5.3. Nos piden que escribamos una función que le pida 
al usuario que ingrese un número positivo. Si el usuario ingresa cualquier 
cosa que no sea lo pedido se le debe informar de su error mediante un mensaje 
y volverle a pedir el número."""

def escribeUnNumero():
   num = input("Escribe un numero: ")

   while num.isdigit() != True:
      print("No es un numero")
      num = input("Escribe un numero: ")
         
escribeUnNumero()
        

            