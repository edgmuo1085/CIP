# Desarrollado por: Edgar Munoz
# Mi primer ventana

#GUI library
import os # Librería para limpiar pantalla
from random import randint, uniform, random
#Gestionar Widgets: Buttons, labels, inputs, etc
from tkinter import ttk
import tkinter as tk

#Definir variables
num = 0
def saludo():
	print("Has hecho clic")

def contar():
	global num
	num += 1
	label.config(text=str(num))
	print(num)

def restar():
	global num
	num -= 1
	label.config(text=str(num))
	print(num)

#os.system("clear") # Borrar pantalla
mi_ventana = tk.Tk()

#icono de ventana
#mi_ventana.iconbitmap('iconos/favicon.ico')
#Titulo
mi_ventana.title("MI PRIMER VENTANA")
#geometry(WxH+X+Y)
mi_ventana.geometry("600x600+500+50")
# Cambiar tamaño de la ventana
mi_ventana.resizable(width=False, height=True)
# background de la ventana
mi_ventana.config(bg="blue")
#label
label = tk.Label(mi_ventana, fg="dark green")
label.pack()

#lambda: se ejecuta la funcion antes de dar clic en el boton
#boton1 = tk.Button(mi_ventana, text="Sumar 1", command=contar).place(x=60, y=40, width=100, height=100)
#boton2 = tk.Button(mi_ventana, text="Restar 1", command=restar).place(x=170, y=40, width=100, height=100)

btn1 = tk.Button(mi_ventana, text="1", command=restar).place(x=10, y=40, width=80, height=80)
btn2 = tk.Button(mi_ventana, text="2", command=restar).place(x=95, y=40, width=80, height=80)
btn3 = tk.Button(mi_ventana, text="3", command=restar).place(x=180, y=40, width=80, height=80)

btn4 = tk.Button(mi_ventana, text="4", command=restar).place(x=10, y=125, width=80, height=80)
btn5 = tk.Button(mi_ventana, text="5", command=restar).place(x=95, y=125, width=80, height=80)
btn6 = tk.Button(mi_ventana, text="6", command=restar).place(x=180, y=125, width=80, height=80)

btn7 = tk.Button(mi_ventana, text="7", command=restar).place(x=10, y=210, width=80, height=80)
btn8 = tk.Button(mi_ventana, text="8", command=restar).place(x=95, y=210, width=80, height=80)
btn9 = tk.Button(mi_ventana, text="9", command=restar).place(x=180, y=210, width=80, height=80)

btn0 = tk.Button(mi_ventana, text="0", command=restar).place(x=10, y=295, width=80, height=80)

btnShow = tk.Button(mi_ventana, text="Show", command=restar).place(x=95, y=295, width=165, height=80)


#Ejecutar ventana
mi_ventana.mainloop()