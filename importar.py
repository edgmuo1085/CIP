# Desarrollado por: Edgar Muñoz
# Importación de librerías

#### Librerias ####
import os # Librería para limpiar pantalla

#### Funciones ####


def numeros(num):
	i=1
	while i <= num:
		if i % 2 == 0:
			print("Número:", i)

		i =i+1
		
	print("\n")


#### MENU ####
os.system("clear") # Borrar pantalla
print("\n .::: SERIE DE NÚMEROS :::. ")
N = int(input("Digite un limite: "))
numeros(N)
