from sshtunnel import SSHTunnelForwarder
import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import *
import threading
from Asistencia import *
from Empleado import *
from Empresa import *

def reloj():
    hora = strftime('%H:%M:%S %p')
    labelReloj.config(text = hora)
    labelReloj.after(1000, reloj)

def mostrarFrameChecador():
    #Borra elementos contenidos en el frame contenedorFrames
    for widget in contenedorFrames.winfo_children():
        widget.destroy()
    
    frameChecador = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameChecador.grid(row=1,column=0, columnspan=2)
    frameChecador.grid_propagate(False) 

    nombreModulo.config(text="Checador")
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
    textoIdEmpleado.bind('<Return>', lambda x: asistencia.insertarAsistencia(textoIdEmpleado, labelNombreEmpleado, db))

def mostrarAltaEmpleados():
    for widget in contenedorFrames.winfo_children():
        widget.destroy()
    
    empleado = Empleado()
    nombreModulo.config(text="Alta Empleado")
    frameAltaEmpleados = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameAltaEmpleados.grid(row=1,column=0, columnspan=2)
    frameAltaEmpleados.grid_propagate(False)
    
    labelVacio = Label(frameAltaEmpleados, text="",bg='white')
    labelVacio.grid(row=0,column=0,pady=30)

    labelIdEmpleado = Label(frameAltaEmpleados, text="ID Empleado:", font=('Verdana',20), bg='white')
    labelIdEmpleado.grid(row=1,column=0, pady=30, sticky=E)
    comandos = db.cursor()
    comandos.execute("SELECT idEmpleado from Empleados ORDER BY fechaRegistro DESC LIMIT 1")
    resultado = comandos.fetchone()
    idEmpleado = resultado[0] + 1
    textoIdEmpleado = Entry(frameAltaEmpleados, bd=5, font=('Verdana',20))
    textoIdEmpleado.insert(0,idEmpleado)
    textoIdEmpleado.config(state='disabled')
    textoIdEmpleado.grid(row=1, column=1, padx=5, pady=30)

    labelNombreEmpleado = Label(frameAltaEmpleados, text="Nombre:", font=('Verdana',20), bg='white')
    labelNombreEmpleado.grid(row=2,column=0, pady=30, sticky=E)
    nombreVar= StringVar()
    textoNombreEmpleado = Entry(frameAltaEmpleados, bd=5, textvariable=nombreVar, font=('Verdana',20))
    textoNombreEmpleado.grid(row=2, column=1, padx=5, pady=30)

    labelApellidoP = Label(frameAltaEmpleados, text="Apellido Paterno:", font=('Verdana',20), bg='white')
    labelApellidoP.grid(row=3,column=0, pady=30, sticky=E)
    apellidoPVar= StringVar()
    textoApellidoP = Entry(frameAltaEmpleados, bd=5, textvariable=apellidoPVar, font=('Verdana',20))
    textoApellidoP.grid(row=3, column=1, padx=5, pady=30)

    labelApellidoM = Label(frameAltaEmpleados, text="Apellido Materno:", font=('Verdana',20), bg='white')
    labelApellidoM.grid(row=4,column=0, pady=30, sticky=E)
    apellidoMVar= StringVar()
    textoApellidoM = Entry(frameAltaEmpleados, bd=5, textvariable=apellidoMVar, font=('Verdana',20))
    textoApellidoM.grid(row=4, column=1, padx=5, pady=30)

    botonRegistrar = Button(frameAltaEmpleados, text="Registrar Empleados", font=('Verdana',20), command=lambda: empleado.altaEmpleado(textoIdEmpleado,textoNombreEmpleado,textoApellidoP,textoApellidoM,db)) 
    botonRegistrar.grid(row=5,column=0, padx=60, pady=70, sticky=W)

    botonBorrar = Button(frameAltaEmpleados, text="Borrar Campos", font=('Verdana',20), command=lambda: empleado.borrar(textoNombreEmpleado,textoApellidoP,textoApellidoM)) 
    botonBorrar.grid(row=5,column=1, pady=70, padx=20, sticky=E)

def mostrarBajaEmpleados():
    for widget in contenedorFrames.winfo_children():
        widget.destroy()
    
    empleado = Empleado()
    nombreModulo.config(text="Baja Empleado")
    frameBajaEmpleados = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameBajaEmpleados.grid(row=1,column=0, columnspan=2)
    frameBajaEmpleados.grid_propagate(False)
    
    labelVacio = Label(frameBajaEmpleados, text="",bg='white')
    labelVacio.grid(row=0,column=0,pady=30)

    labelIdEmpleado = Label(frameBajaEmpleados, text="ID Empleado:", font=('Verdana',20), bg='white')
    labelIdEmpleado.grid(row=1,column=0, pady=30, sticky=E)
    idVar= StringVar()
    textoIdEmpleado = Entry(frameBajaEmpleados, bd=5, font=('Verdana',20), textvariable=idVar)
    textoIdEmpleado.grid(row=1, column=1, padx=5, pady=30)
    textoIdEmpleado.bind('<Return>', lambda x: empleado.consultarEmpleado(textoIdEmpleado, textoNombreEmpleado, textoApellidoP, textoApellidoM, db))

    labelNombreEmpleado = Label(frameBajaEmpleados, text="Nombre:", font=('Verdana',20), bg='white')
    labelNombreEmpleado.grid(row=2,column=0, pady=30, sticky=E)
    textoNombreEmpleado = Entry(frameBajaEmpleados, bd=5, font=('Verdana',20), state='disabled')
    textoNombreEmpleado.grid(row=2, column=1, padx=5, pady=30)

    labelApellidoP = Label(frameBajaEmpleados, text="Apellido Paterno:", font=('Verdana',20), bg='white')
    labelApellidoP.grid(row=3,column=0, pady=30, sticky=E)
    textoApellidoP = Entry(frameBajaEmpleados, bd=5, font=('Verdana',20), state='disabled')
    textoApellidoP.grid(row=3, column=1, padx=5, pady=30)

    labelApellidoM = Label(frameBajaEmpleados, text="Apellido Materno:", font=('Verdana',20), bg='white')
    labelApellidoM.grid(row=4,column=0, pady=30, sticky=E)
    textoApellidoM = Entry(frameBajaEmpleados, bd=5, font=('Verdana',20), state='disabled')
    textoApellidoM.grid(row=4, column=1, padx=5, pady=30)

    botonRegistrar = Button(frameBajaEmpleados, text="Baja Empleado", font=('Verdana',20), command=lambda: empleado.bajaEmpleado(textoIdEmpleado,textoNombreEmpleado,textoApellidoP,textoApellidoM,db)) 
    botonRegistrar.grid(row=5,column=0, padx=90, pady=70, sticky=W)

    botonBorrar = Button(frameBajaEmpleados, text="Borrar Campos", font=('Verdana',20), command=lambda: empleado.borrarAlterno(textoIdEmpleado,textoNombreEmpleado,textoApellidoP,textoApellidoM)) 
    botonBorrar.grid(row=5,column=1, pady=70, padx=20, sticky=E)

def mostrarModificarEmpleados():
    for widget in contenedorFrames.winfo_children():
        widget.destroy()
    
    empleado = Empleado()
    nombreModulo.config(text="Modificar Empleado")
    frameModificarEmpleados = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameModificarEmpleados.grid(row=1,column=0, columnspan=2)
    frameModificarEmpleados.grid_propagate(False)

    labelIdEmpleado = Label(frameModificarEmpleados, text="ID Empleado:", font=('Verdana',20), bg='white')
    labelIdEmpleado.grid(row=1,column=0, pady=30, sticky=E)
    idVar= StringVar()
    textoIdEmpleado = Entry(frameModificarEmpleados, bd=5, font=('Verdana',20), textvariable=idVar)
    textoIdEmpleado.grid(row=1, column=1, padx=5, pady=30)
    textoIdEmpleado.bind('<Return>', lambda x: empleado.consultarEmpleadoAlterno(textoIdEmpleado, textoNombreEmpleado, textoApellidoP, textoApellidoM, comboEstado, db))

    labelNombreEmpleado = Label(frameModificarEmpleados, text="Nombre:", font=('Verdana',20), bg='white')
    labelNombreEmpleado.grid(row=2,column=0, pady=30, sticky=E)
    nombreVar= StringVar()
    textoNombreEmpleado = Entry(frameModificarEmpleados, bd=5, textvariable=nombreVar, font=('Verdana',20), state='disabled')
    textoNombreEmpleado.grid(row=2, column=1, padx=5, pady=30)

    labelApellidoP = Label(frameModificarEmpleados, text="Apellido Paterno:", font=('Verdana',20), bg='white')
    labelApellidoP.grid(row=3,column=0, pady=30, sticky=E)
    apellidoPVar= StringVar()
    textoApellidoP = Entry(frameModificarEmpleados, bd=5, textvariable=apellidoPVar, font=('Verdana',20), state='disabled')
    textoApellidoP.grid(row=3, column=1, padx=5, pady=30)

    labelApellidoM = Label(frameModificarEmpleados, text="Apellido Materno:", font=('Verdana',20), bg='white')
    labelApellidoM.grid(row=4,column=0, pady=30, sticky=E)
    apellidoMVar= StringVar()
    textoApellidoM = Entry(frameModificarEmpleados, bd=5, textvariable=apellidoMVar, font=('Verdana',20), state='disabled')
    textoApellidoM.grid(row=4, column=1, padx=5, pady=30)

    labelEstado = Label(frameModificarEmpleados, text="Estado:", font=('Verdana',20), bg='white')
    labelEstado.grid(row=5,column=0, pady=30, sticky=E)
    comboEstado= ttk.Combobox(frameModificarEmpleados, state='readonly', font=('Verdana',20))
    comboEstado['values'] = ('Activo','Baja')
    comboEstado.grid(row=5, column=1, padx=5, pady=30)
    comboEstado.current(0)

    botonRegistrar = Button(frameModificarEmpleados, text="Modificar Empleado", font=('Verdana',20), command=lambda: empleado.modificarEmpleado(textoIdEmpleado,textoNombreEmpleado,textoApellidoP,textoApellidoM,comboEstado,db)) 
    botonRegistrar.grid(row=6,column=0, padx=60, pady=70, sticky=W)

    botonBorrar = Button(frameModificarEmpleados, text="Borrar Campos", font=('Verdana',20), command=lambda: empleado.borrarAlterno(textoIdEmpleado,textoNombreEmpleado,textoApellidoP,textoApellidoM)) 
    botonBorrar.grid(row=6,column=1, pady=70, padx=20, sticky=E)

def mostrarRegistrarEmpresa():
    for widget in contenedorFrames.winfo_children():
            widget.destroy()
    
    comandos = db.cursor()
    comandos.execute('SELECT * from Empresa')
    respuesta = comandos.fetchone()
    nombreModulo.config(text="Registrar Empresa")

    if respuesta:
        mensaje = messagebox.showerror('¡Error!','Ya hay una empresa registrada.')
    else:
        empresa = Empresa()
        
        frameRegistrarEmpresa = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
        frameRegistrarEmpresa.grid(row=1,column=0, columnspan=2)
        frameRegistrarEmpresa.grid_propagate(False)

        labelRFC = Label(frameRegistrarEmpresa, text="RFC:", font=('Verdana',20), bg='white')
        labelRFC.grid(row=1,column=0, pady=30, sticky=E)
        RFCVar= StringVar()
        textoRFC = Entry(frameRegistrarEmpresa, bd=5, font=('Verdana',20), textvariable=RFCVar)
        textoRFC.grid(row=1, column=1, padx=5, pady=30)

        labelNombreEmpresa = Label(frameRegistrarEmpresa, text="Nombre:", font=('Verdana',20), bg='white')
        labelNombreEmpresa.grid(row=2,column=0, pady=30, sticky=E)
        nombreVar= StringVar()
        textoNombreEmpresa = Entry(frameRegistrarEmpresa, bd=5, textvariable=nombreVar, font=('Verdana',20))
        textoNombreEmpresa.grid(row=2, column=1, padx=5, pady=30)

        labelDireccion = Label(frameRegistrarEmpresa, text="Dirección:", font=('Verdana',20), bg='white')
        labelDireccion.grid(row=3,column=0, pady=30, sticky=E)
        apellidoPVar= StringVar()
        textoDireccion = Entry(frameRegistrarEmpresa, bd=5, textvariable=apellidoPVar, font=('Verdana',20))
        textoDireccion.grid(row=3, column=1, padx=5, pady=30)

        labelTelefono = Label(frameRegistrarEmpresa, text="Teléfono:", font=('Verdana',20), bg='white')
        labelTelefono.grid(row=4,column=0, pady=30, sticky=E)
        telefonoVar= StringVar()
        textoTelefono = Entry(frameRegistrarEmpresa, bd=5, textvariable=telefonoVar, font=('Verdana',20))
        textoTelefono.grid(row=4, column=1, padx=5, pady=30)

        labelEmail = Label(frameRegistrarEmpresa, text="E-mail:", font=('Verdana',20), bg='white')
        labelEmail.grid(row=5,column=0, pady=30, sticky=E)
        emailVar = StringVar()
        textoEmail = Entry(frameRegistrarEmpresa, bd=5, textvariable=emailVar, font=('Verdana',20))
        textoEmail.grid(row=5, column=1, padx=5, pady=30)

        botonRegistrar = Button(frameRegistrarEmpresa, text="Registrar Empresa", font=('Verdana',20), command=lambda: empresa.registrarEmpresa(textoRFC,textoNombreEmpresa,textoDireccion,textoTelefono,textoEmail,botonRegistrar, db)) 
        botonRegistrar.grid(row=6,column=0, padx=60, pady=70, sticky=W)

def mostrarConsultarEmpresa():
    for widget in contenedorFrames.winfo_children():
        widget.destroy()
    
    empresa = Empresa()

    rfc,nombreEmpresa,direccion,telefono,email = empresa.consultarEmpresa(db)

    nombreModulo.config(text="Consultar Empresa")
    frameConsultarEmpresa = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameConsultarEmpresa.grid(row=1,column=0, columnspan=2)
    frameConsultarEmpresa.grid_propagate(False)

    labelRFC = Label(frameConsultarEmpresa, text="RFC:", font=('Verdana',20), bg='white')
    labelRFC.grid(row=1,column=0, pady=30, sticky=E)
    textoRFC = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
    textoRFC.insert(0,rfc)
    textoRFC.config(state = 'disabled')
    textoRFC.grid(row=1, column=1, padx=5, pady=30)
    
    labelNombreEmpresa = Label(frameConsultarEmpresa, text="Nombre Empresa:", font=('Verdana',20), bg='white')
    labelNombreEmpresa.grid(row=2,column=0, pady=30, sticky=E)
    textoNombreEmpresa = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
    textoNombreEmpresa.insert(0,nombreEmpresa)
    textoNombreEmpresa.config(state = 'disabled')
    textoNombreEmpresa.grid(row=2, column=1, padx=5, pady=30)

    labelDireccion = Label(frameConsultarEmpresa, text="Dirección:", font=('Verdana',20), bg='white')
    labelDireccion.grid(row=3,column=0, pady=30, sticky=E)
    textoDireccion = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
    textoDireccion.insert(0,direccion)
    textoDireccion.config(state = 'disabled')
    textoDireccion.grid(row=3, column=1, padx=5, pady=30)

    labelTelefono = Label(frameConsultarEmpresa, text="Teléfono:", font=('Verdana',20), bg='white')
    labelTelefono.grid(row=4,column=0, pady=30, sticky=E)
    textoTelefono = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
    textoTelefono.insert(0,telefono)
    textoTelefono.config(state = 'disabled')
    textoTelefono.grid(row=4, column=1, padx=5, pady=30)

    labelEmail = Label(frameConsultarEmpresa, text="Email:", font=('Verdana',20), bg='white')
    labelEmail.grid(row=5,column=0, pady=30, sticky=E)
    textoEmail = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
    textoEmail.insert(0,email)
    textoEmail.config(state = 'disabled')
    textoEmail.grid(row=5, column=1, padx=5, pady=30)

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
ventanaPrincipal.title("Checador")
ventanaAncho = ventanaPrincipal.winfo_reqwidth()
ventanaLargo = ventanaPrincipal.winfo_reqheight()
posicionDerecha = int(ventanaPrincipal.winfo_screenwidth()/2 - ventanaAncho/0.4)
posicionAbajo = int(ventanaPrincipal.winfo_screenheight()/2 - ventanaLargo/0.45)
ventanaPrincipal.geometry("1000x800+{}+{}".format(posicionDerecha, posicionAbajo))
ventanaPrincipal.resizable(0,0)

asistencia = Asistencia()
archivofoto = PhotoImage(file = "iconos/persona.png")

contenedorBotones = Frame(ventanaPrincipal, width=100, height=800, bg='white')
contenedorBotones.grid(row=0,column=0, rowspan=5, pady=20, padx=10)

nombreModulo = Label(ventanaPrincipal, text="Checador", font=('Verdana',16), bg='white')
nombreModulo.grid(row=0,column=1, sticky='SW', pady=5)

labelReloj = Label(ventanaPrincipal, font=('Verdana', 16, 'bold'), fg='black', bg='white')
labelReloj.grid(row=0,column=2, sticky='SE',pady=5)
reloj()

contenedorFrames = Frame(ventanaPrincipal, width=900, height=800, bg='white')
contenedorFrames.grid(row=1,column=1, rowspan=4, columnspan=2)

iconoInicio = PhotoImage(file = "iconos/home.png").subsample(8,8)
iconoAlta = PhotoImage(file = "iconos/up-arrow.png").subsample(8,8)
iconoBaja = PhotoImage(file = "iconos/down-arrow.png").subsample(8,8)
iconoConsulta = PhotoImage(file = "iconos/search.png").subsample(8,8)
iconoReporte = PhotoImage(file = "iconos/file.png").subsample(8,8)
iconoEmpresa = PhotoImage(file = "iconos/edificio-de-oficinas.png").subsample(8,8)

botonInicio = Button(contenedorBotones, text = "Inicio", image = iconoInicio, bg='white', relief='flat', command=mostrarFrameChecador)
botonInicio.grid(row=0, column=0, pady=25, padx=20)
botonAlta = Button(contenedorBotones, text = "Alta", image = iconoAlta, bg='white', relief='flat', command=mostrarAltaEmpleados)
botonAlta.grid(row=1, column=0, pady=25, padx=20)
botonBaja = Button(contenedorBotones, text = "Baja", image = iconoBaja, bg='white', relief='flat', command=mostrarBajaEmpleados)
botonBaja.grid(row=2, column=0, pady=25, padx=20)
botonConsulta = Button(contenedorBotones, text = "Consulta", image = iconoConsulta, bg='white', relief='flat', command=mostrarModificarEmpleados)
botonConsulta.grid(row=3, column=0, pady=25, padx=20)
botonReporte = Button(contenedorBotones, text = "Reporte", image = iconoReporte, bg='white', relief='flat', command=mostrarRegistrarEmpresa)
botonReporte.grid(row=4, column=0, pady=25, padx=20)
botonEmpresa = Button(contenedorBotones, text = "Empresa", image = iconoEmpresa, bg='white', relief='flat', command=mostrarConsultarEmpresa)
botonEmpresa.grid(row=5, column=0, pady=25, padx=20)

mostrarFrameChecador()

ventanaPrincipal.config(cursor="arrow")
ventanaPrincipal.config(bg="white")

ventanaPrincipal.mainloop()

db.close()
server.stop()