# El usuario debe de adivinar un numero entre 0 y 10. El programa debera pedir al usuario que 
# que introduzca un numero y debe de decir si ha acertado, si el numero adivinar es menor o mayor
# que el que ha introducido.

# Edmoun
def adivinar():
    numeroAdivinar = 6
    num = int(input("Escribe un numero: "))
    if (num == numeroAdivinar):
        print("Felicidades haz acertado")
        return True
    elif(num <= numeroAdivinar):
        print("El numero introducido es menor")
        return False
    elif(num >= numeroAdivinar):
        print("El numero introducido es mayor")
        return False
    else:
        print("El numero introducido tiene que ser menor o igual que 10")
while(True):
    if(adivinar()):
        break
    
        

