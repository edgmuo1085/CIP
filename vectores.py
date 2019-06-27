#vectores

import os # Librería para limpiar pantalla
from random import randint, uniform, random

numeros = []
N = 0
i = 0

N = int(input("Ingrese cantidad de numeros a generar: "))
while i< N:
	Na = randint(1,100)
	numeros.append(Na)
	i += 1
key = input(" ::: Presione cualquier tecla para ver el vector :::")
os.system("clear") # Borrar pantalla
print("\nEl vector generado es: ",numeros)
print("\nEl elemento en la pos es: ",numeros[0])
print("\nLa cantidad de elementos generados: ",len(numeros))