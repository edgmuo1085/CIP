# Desarrollado por: Edgar Muñoz
# Número aleatorios

#### Librerias ####
import os # Librería para limpiar pantalla
from random import randint, uniform, random

#### Funciones ####


def numeros_aleatorios(num, opcion=1):
	par_positivo = 0
	par_negativo = 0
	impar_positivo = 0
	impar_negativo = 0
	real_positivo = 0
	real_negativo = 0
	imreal_positivo = 0
	imreal_negativo = 0

	if opcion == 1:
		i = 1
		while i <= num:
			alea = randint(-100, 100)
			print("aleatorios: ",alea)
			if alea >= 0:
				if alea % 2 == 0:
					par_positivo = par_positivo + 1 # almacena entero positivo
				else:
					impar_positivo = impar_positivo + 1
			else:
				if alea % 2 == 0:
					par_negativo = par_negativo + 1 # almacena entero negativo
				else:
					impar_negativo = impar_negativo + 1

			i = i + 1
		print("\nPares positivos: ",par_positivo)
		print("Pares negativo: ",par_negativo)
		print("Impares positivos: ",impar_positivo)
		print("Impares negativo: ",impar_negativo)

	else:
		i = 1
		while i <= num:
			alea = uniform(-100, 100)
			print("aleatorio real: ",alea)
			if alea >= 0:
				if alea % 2 == 0:
					real_positivo = real_positivo + 1 # almacena real positivo
				else:
					imreal_positivo = imreal_positivo + 1
			else:
				if alea % 2 == 0:
					real_negativo = real_negativo + 1 # almacena real negativo
				else:
					imreal_negativo = imreal_negativo + 1

			i = i + 1

		print("\nReal positivos: ",real_positivo)
		print("Reales negativo: ",real_negativo)
		print("Imreales positivos: ",imreal_positivo)
		print("Imreales negativo: ",imreal_negativo)


#### MENU ####
os.system("clear") # Borrar pantalla
print("\n\t.::: NÚMEROS ALEATORIOS :::. ")
N  = int(input("\nDatos a generar: "))
print("\n[1]. Números enteros ")
print("[2]. Números reales ")
OP = int(input("\n.:: Digite opción: "))
numeros_aleatorios(N,OP)