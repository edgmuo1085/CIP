#vectores

import os # Librería para limpiar pantalla
from random import randint, uniform, random

numeros = []
suma = 0
N = 0


while True:
	N = int(input("Ingrese el numero: "))
	tamaño = len(numeros)

	if tamaño == 10:
		print(" ::: Fin del vector :::")
		break

	if tamaño >= 2:
		suma = numeros[tamaño-2] + numeros[tamaño-1]

	if N == suma:
		print(" ::: El valor no es permitido\n ::: Ingrese nuevamente un numero\n")

	else :
		numeros.append(N)

print("valores: ",numeros)






	#i += 1
#key = input(" ::: Presione cualquier tecla para ver el vector :::")
#os.system("clear") # Borrar pantalla

#print("\nEl vector generado es: ",numeros)
#print("\nEl elemento en la pos es: ",numeros[0])
#print("\nLa cantidad de elementos generados: ",len(numeros))