"""Ejercicio 3.8.1. Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos."""

def cantidad_horas_min_segs():
    segundos = float(input("Ingrese Cantidad en Segundos : "))
    horas = round(segundos/3600)
    minutos = round(segundos/60)
    segs = round(segundos*1)
    print("Horas   : ",horas)
    print("Minutos : ",minutos)
    print("segundos : ",segs)

def cantidad_segundos():
    horas = int(input("Ingrese una hora: "))
    min = int(input("Ingrese un minuto: "))
    segs = int(input("Ingrese un segs: "))
    segundos = horas*3600
    segundo = min*60
    segund = segs*1
    print("Horas : ",segundos)
    print("Min : ",segundo)
    print("segundos : ",segund)

cantidad_segundos(), cantidad_horas_min_segs()
