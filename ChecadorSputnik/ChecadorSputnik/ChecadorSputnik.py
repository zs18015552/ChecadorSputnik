from sshtunnel import SSHTunnelForwarder
import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import *
from Asistencia import *

def validarEntrada(caracter,cadena):
    if len(cadena) > 7:
        return False
    return caracter.isdecimal()

def reloj():
    hora = strftime('%H:%M:%S %p')
    labelReloj.config(text = hora)
    labelReloj.after(1000, reloj)

def mostrarFrameChecador():
    #Borra elementos contenidos en el frame contenedorFrames
    for widget in contenedorFrames.winfo_children():
        widget.destroy()
    
    frameChecador = Frame(contenedorFrames, width=965, height=740, bd=5, bg='white', relief='ridge')
    frameChecador.grid(row=1,column=0, columnspan=2, padx=15)
    frameChecador.grid_propagate(False) 

    nombreModulo.config(text="Checador")
    canvasFotoEmpleado = Canvas(frameChecador, width=256, height=260, bg='white')
    canvasFotoEmpleado.grid(row=0,column=0, padx=350, pady=40)
    fotoEmpleado = canvasFotoEmpleado.create_image(130, 130, image=archivofoto)
    
    labelNombreEmpleado = Label(frameChecador, text="<<Nombre>>", font=('Verdana',24), bg='white', fg='gray')
    labelNombreEmpleado.grid(row=1, column=0, columnspan=2)

    labelVacio = Label(frameChecador, text="", font=('Verdana',24), bg='white')
    labelVacio.grid(row=2, column=0, columnspan=2, pady=10)

    labelIdEmpleado = Label(frameChecador, text="ID Empleado", font=('Verdana',24), bg='white')
    labelIdEmpleado.grid(row=3, column=0, columnspan=2)

    textoIdEmpleado = Entry(frameChecador, bd=5, validate='key', font=('Verdana',24), show='*')
    textoIdEmpleado['validatecommand'] = (textoIdEmpleado.register(validarEntrada),'%S','%P')
    textoIdEmpleado.grid(row=4, column=0, columnspan=2)
    textoIdEmpleado.bind('<Return>', lambda x: asistencia.insertarAsistencia(textoIdEmpleado, labelNombreEmpleado, labelMensaje, db))

    labelMensaje = Label(frameChecador, text="", font=('Verdana',24), bg='white')
    labelMensaje.grid(row=5, column=0, columnspan=2, pady=10)

#Conexión a la base de datos 
server = SSHTunnelForwarder(("198.54.125.222", 21098),
                                    ssh_host_key=None,
                                    ssh_username="axclzgpy",
                                    ssh_password="30dpr3538T@#alex",
                                    remote_bind_address=("127.0.0.1", 3306))

server.start()

try:
    db=mysql.connect(user='axclzgpy_sputnik',
                     password='jU0x3CV}Dv;c@wg67L',
                     host="127.0.0.1",
                     port=server.local_bind_port, 
                     database='axclzgpy_sputnik-VII')
    print("Conexión exitosa.")
    
except Exception as e:
    print(e)
    print("Conexión fallida")

#Elementos principales de la GUI    
ventanaPrincipal = Tk()
ventanaPrincipal.title("Checador Sputnik")
ventanaAncho = ventanaPrincipal.winfo_reqwidth()
ventanaLargo = ventanaPrincipal.winfo_reqheight()
posicionDerecha = int(ventanaPrincipal.winfo_screenwidth()/2 - ventanaAncho/0.4)
posicionAbajo = int(ventanaPrincipal.winfo_screenheight()/2 - ventanaLargo/0.45)
ventanaPrincipal.geometry("1000x800+{}+{}".format(posicionDerecha, posicionAbajo))
ventanaPrincipal.resizable(0,0)

asistencia = Asistencia()
archivofoto = PhotoImage(file = ".iconos/employee.png").subsample(2,2)

nombreModulo = Label(ventanaPrincipal, text="Checador", font=('Verdana',16), bg='white')
nombreModulo.grid(row=0,column=1, sticky='W', pady=5, padx=15)

labelReloj = Label(ventanaPrincipal, font=('Verdana', 16, 'bold'), fg='black', bg='white')
labelReloj.grid(row=0,column=2, sticky='E')
reloj()

contenedorFrames = Frame(ventanaPrincipal, width=990, height=800, bg='white')
contenedorFrames.grid(row=1,column=1, rowspan=4, columnspan=2)

mostrarFrameChecador()

ventanaPrincipal.config(cursor="arrow")
ventanaPrincipal.config(bg="white")

ventanaPrincipal.mainloop()

db.close()
server.stop()