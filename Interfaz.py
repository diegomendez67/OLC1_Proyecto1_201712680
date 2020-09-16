from tkinter import *
from tkinter import scrolledtext
import tkinter, time, base64, imaplib, smtplib
from imaplib import *
from tkinter import *
from tkinter.ttk import *
from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
#from Analizador_Lexico import analizador
import os.path
from AnalizadorHTML import analizador
from AnalizadorCSS import analizadorCSS

#funciones del menu

archivo =""
def ejecutar():


    fname = entradas.get(1.0, END)
    tipo = os.path.splitext(archivo)[1]
    salidas.delete(1.0,END)
    ent = os.path.split(archivo)[1]

    if tipo in ".html":
        salidas.delete(1.0, END)
        html = analizador
        messagebox.showinfo(message="analizando html")
        html.analizador(fname)
        salidas.insert(INSERT,html.Mandar_Nuevo())
        html.ReporteErrores()

    elif tipo in ".css":
        salidas.delete(1.0, END)
        css = analizadorCSS
        messagebox.showinfo(message="analizando css")
        css.analizador(fname)
        salidas.insert(INSERT, css.consola())
        salidas.insert(INSERT, css.Mandar_Nuevo())
        css.ReporteErrores()

    os.system("Reporte.html")




def AbrirReporte():
    an = analizador
    an.ReporteErrores()
    os.system("Reporte.html")


def nuevo():
    global archivo
    entradas.delete(1.0, END)#ELIMINAR EL CONTENIDO
    archivo = ""

def abrir():
    global archivo

    archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "C:/")
    print(archivo)
    file = open(archivo)
    content = file.read()

    entradas.delete(1.0, END)
    entradas.insert(INSERT, content)
    file.close()

def guardar():
    global archivo
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w")
        guardarc.write(entradas.get(1.0, END))
        guardarc.close()

def guardarComo():
    global archivo
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/")
    fguardar = open(guardar, "w+")
    fguardar.write(entradas.get(1.0, END))
    fguardar.close()
    archivo = guardar


#CREANDO LA VENTANA POR DEFECTO
window = Tk()
window.title("ML WEB EDITOR V[Mad1.Ly]")
window.geometry('1000x500')


#declaracion de variables para menu principal
menu = Menu(window)
Archivos = Menu(menu)
Guardar = Menu(menu)
Ejecutar = Menu(menu)
Reporte = Menu(menu)


#declaracion de items para seccion Archivos
Archivos.add_command(label = 'Nuevo', command = nuevo)
Archivos.add_command(label = 'Abrir', command = abrir)

#declaracion de items para seccion Archivos
Guardar.add_command(label = 'Guardar', command = guardar)
Guardar.add_command(label = 'Guardar Como', command = guardarComo)

#declaracion de items para seccion Ejecutar
Ejecutar.add_command(label = 'Analizar', command = ejecutar)

#declaracion de items para reportes:
Reporte.add_command(label = "Mostrar ultimo reporte", command =  AbrirReporte)

#agregando secciones a la barra de Menu
menu.add_cascade(label = 'Archivo', menu = Archivos)
menu.add_cascade(label = 'Guardar', menu = Guardar)
menu.add_cascade(label = 'Ejecutar', menu = Ejecutar)
menu.add_cascade(label = 'Reportes', menu= Reporte)

#Agregar un Scrolled text para ingreso de datos a la ventana
entradas = scrolledtext.ScrolledText(window,width=60,height=25)
entradas.grid(column=0,row=0)
entradas.place(x=10, y =50)

#Mostrar mesaje de bienvenida
entradas.insert(INSERT,'          //Todo el codigo aca')

#Agregar un Scrolled text para salida de datos a la ventana
salidas = scrolledtext.ScrolledText(window,width=60,height=25)
salidas.grid(column=0,row=0)
salidas.place(x=500, y =50)
salidas.config(background = 'gray')
#Mostrar mesaje de bienvenida
salidas.insert(INSERT,'...waiting for orders, showing output files and logs ')

#Cargando menu a la pantalla e incluyendo propiedades de ventana
window.config(menu = menu)
window.mainloop()
