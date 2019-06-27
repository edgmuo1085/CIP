# Desarrollado por: Edgar Munoz
# Mi primer ventana

#GUI library
import os # Librería para limpiar pantalla
from random import randint, uniform, random
from tkinter import ttk
import tkinter as tk


#os.system("clear") # Borrar pantalla
mi_ventana = tk.Tk()

#icono
#mi_ventana.iconbitmap('iconos/favicon.ico')
#Titulo
mi_ventana.title("MI PRIMER VENTANA")
#geometry(WxH+X+Y)
mi_ventana.geometry("600x600+500+50")
# Cambiar tamaño de la ventana
mi_ventana.resizable(width=False, height=True)
# background de la ventana
mi_ventana.config(bg="#CFACAC")
boton = tk.Button(mi_ventana, text="Ejecutar").place(x=60, y=40, width=100, height=100)
#Ejecutar ventana
mi_ventana.mainloop()