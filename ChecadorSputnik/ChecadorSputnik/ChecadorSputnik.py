from tkinter import *
from time import *
import threading
from Asistencia import *

archivofoto = ''

def reloj():
    hora = strftime('%H:%M:%S %p')
    labelReloj.config(text = hora)
    labelReloj.after(1000, reloj)

def mostrarFrameChecador():
    frameChecador = Frame(contenedorFrames, width=850, height=700)
    frameChecador.config(bd=5)
    frameChecador.config(bg='white')
    frameChecador.config(relief="ridge")
    frameChecador.grid(row=1,column=0, columnspan=2)
    frameChecador.grid_propagate(False)

    canvasFotoEmpleado = Canvas(frameChecador, width=256, height=260, bg='white')
    canvasFotoEmpleado.grid(row=0,column=0, padx=290, pady=40)
    fotoEmpleado = canvasFotoEmpleado.create_image(150, 132, image=archivofoto)
    
    labelNombreEmpleado = Label(frameChecador, text="<<Nombre>>", font=('Verdana',24), bg='white', fg='gray')
    labelNombreEmpleado.grid(row=1, column=0, columnspan=2)

    labelVacio = Label(frameChecador, text="", font=('Verdana',24), bg='white')
    labelVacio.grid(row=2, column=0, columnspan=2, pady=10)

    labelIdEmpleado = Label(frameChecador, text="ID Empleado", font=('Verdana',24), bg='white')
    labelIdEmpleado.grid(row=3, column=0, columnspan=2)

    idvar = StringVar()
    textoIdEmpleado = Entry(frameChecador, bd=5, textvariable=idvar, font=('Verdana',24), show='*')
    textoIdEmpleado.grid(row=4, column=0, columnspan=2)
    textoIdEmpleado.bind('<Return>', lambda x: asistencia.insertarAsistencia(textoIdEmpleado.get(), labelNombreEmpleado))

ventanaPrincipal = Tk()
ventanaPrincipal.title("Checador")
ventanaPrincipal.geometry("1000x800")
ventanaPrincipal.resizable(0,0)

asistencia = Asistencia()
archivofoto = PhotoImage(file = "iconos/persona.png")

contenedorFrames = Frame(ventanaPrincipal, width=900, height=800)
contenedorFrames.grid(row=0,column=1, pady=20)
contenedorFrames.config(bg="white")

contenedorBotones = Frame(ventanaPrincipal, width=100, height=800)
contenedorBotones.grid(row=0,column=0)
contenedorBotones.config(bg="white")

nombreModulo = Label(contenedorFrames, text="Checador", font=('Verdana',16), bg='white')
nombreModulo.grid(row=0,column=0, sticky='W')

labelReloj = Label(contenedorFrames, font=('Verdana', 16, 'bold'), fg='black', bg='white')
labelReloj.grid(row=0,column=1, sticky='E')
reloj()

iconoInicio = PhotoImage(file = "iconos/home.png").subsample(6,6)
iconoAlta = PhotoImage(file = "iconos/up-arrow.png").subsample(6,6)
iconoBaja = PhotoImage(file = "iconos/down-arrow.png").subsample(6,6)
iconoConsulta = PhotoImage(file = "iconos/search.png").subsample(6,6)
iconoReporte = PhotoImage(file = "iconos/file.png").subsample(6,6)

botonInicio = Button(contenedorBotones, text = "Inicio", image = iconoInicio, bg='white', relief='flat')
botonInicio.grid(row=0, column=0, pady=25, padx=20)
botonAlta = Button(contenedorBotones, text = "Alta", image = iconoAlta, bg='white', relief='flat')
botonAlta.grid(row=1, column=0, pady=25, padx=20)
botonBaja = Button(contenedorBotones, text = "Baja", image = iconoBaja, bg='white', relief='flat')
botonBaja.grid(row=2, column=0, pady=25, padx=20)
botonConsulta = Button(contenedorBotones, text = "Consulta", image = iconoConsulta, bg='white', relief='flat')
botonConsulta.grid(row=3, column=0, pady=25, padx=20)
botonReporte = Button(contenedorBotones, text = "Reporte", image = iconoReporte, bg='white', relief='flat')
botonReporte.grid(row=4, column=0, pady=25, padx=20)

mostrarFrameChecador()

ventanaPrincipal.config(cursor="arrow")
ventanaPrincipal.config(bg="white")

ventanaPrincipal.mainloop()
