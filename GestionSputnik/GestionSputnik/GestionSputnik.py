from sshtunnel import SSHTunnelForwarder
import mysql.connector
from tkinter import *
from time import *
from tkinter import ttk 
from tkinter import messagebox
from Administrador import *
from DiaFestivo import *
from DiaExcepcion import *
from Horario import *
from Empleado import *
from Empresa import *
from Reporte import *
from tkcalendar import Calendar, DateEntry

def validarEntrada(caracter,cadena):
    if len(cadena) > 10:
        return False
    return caracter.isdecimal()

def cerrarSesion():
    mensaje = messagebox.askquestion('Cerrar sesión','¿Desea cerrar sesión?')

    if mensaje == 'yes':
        for widget in contenedorFrames.winfo_children():
            widget.destroy()

        mostrarIniciarSesion()

def mostrarMenuEmpleado():
    for widget in contenedorFrames.winfo_children():
        widget.destroy()

    nombreModulo.config(text="Menú Empleado")
    frameMenuEmpleados = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameMenuEmpleados.grid(row=1, column=0, columnspan=2)
    frameMenuEmpleados.grid_propagate(False)

    labelVacio = Label(frameMenuEmpleados, text="", font=('Verdana',20), bg='white')
    labelVacio.grid(row=0, column=0, pady=70, padx=10, sticky=E)

    botonAgregar = Button(frameMenuEmpleados, text = "Agregar Empleado", image = iconoAgregar, bg='white', relief='flat', command=mostrarAltaEmpleado)
    botonAgregar.grid(row=1, column=1, pady=20, padx=40)
    labelAgregar = Label(frameMenuEmpleados, text="Alta Empleado", font=('Verdana',14), bg='white')
    labelAgregar.grid(row=2, column=1)
    botonModificar = Button(frameMenuEmpleados, text = "Modificar Empleado", image = iconoModificar, bg='white', relief='flat', command = mostrarModificarEmpleado)
    botonModificar.grid(row=1, column=2, pady=20, padx=50)
    labelModificar = Label(frameMenuEmpleados, text="Modificar Empleado", font=('Verdana',14), bg='white')
    labelModificar.grid(row=2, column=2)
    botonConsultar = Button(frameMenuEmpleados, text = "Consultar Empleados", image = iconoConsultar, bg='white', relief='flat', command=mostrarConsultarEmpleados)
    botonConsultar.grid(row=1, column=3, pady=20, padx=40)
    labelConsultar = Label(frameMenuEmpleados, text="Consultar Empleados", font=('Verdana',14), bg='white')
    labelConsultar.grid(row=2, column=3)

def mostrarMenuHorario():
    for widget in contenedorFrames.winfo_children():
        widget.destroy()

    nombreModulo.config(text="Menú Horario")
    frameMenuHorario = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameMenuHorario.grid(row=1, column=0, columnspan=2)
    frameMenuHorario.grid_propagate(False)

    labelVacio = Label(frameMenuHorario, text="", font=('Verdana',20), bg='white')
    labelVacio.grid(row=0, column=0, pady=70, padx=10, sticky=E)

    labelVacio2 = Label(frameMenuHorario, text="", font=('Verdana',20), bg='white')
    labelVacio2.grid(row=1, column=0, padx=10, sticky=E)

    botonAgregar = Button(frameMenuHorario, text = "Registrar Horario", image = iconoAgregar, bg='white', relief='flat', command=mostrarRegistrarHorarios)
    botonAgregar.grid(row=1, column=1, pady=20, padx=40)
    labelAgregar = Label(frameMenuHorario, text="Registrar Horario", font=('Verdana',14), bg='white')
    labelAgregar.grid(row=2, column=1)
    botonEliminar = Button(frameMenuHorario, text = "Eliminar Horario", image = iconoEliminar, bg='white', relief='flat', command=mostrarEliminarHorarios)
    botonEliminar.grid(row=1, column=2, pady=20, padx=50)
    labelEliminar = Label(frameMenuHorario, text="Eliminar Horario", font=('Verdana',14), bg='white')
    labelEliminar.grid(row=2, column=2)
    botonConsultar = Button(frameMenuHorario, text = "Consultar Horario", image = iconoConsultar, bg='white', relief='flat', command=mostrarConsultarHorarios)
    botonConsultar.grid(row=1, column=3, pady=20, padx=40)
    labelConsultar = Label(frameMenuHorario, text="Consultar Horario", font=('Verdana',14), bg='white')
    labelConsultar.grid(row=2, column=3)

def mostrarMenuDiaFestivo():
    for widget in contenedorFrames.winfo_children():
        widget.destroy()

    nombreModulo.config(text="Menú Día Festivo")
    frameMenuDiaFestivo = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameMenuDiaFestivo.grid(row=1, column=0, columnspan=2)
    frameMenuDiaFestivo.grid_propagate(False)

    labelVacio = Label(frameMenuDiaFestivo, text="", font=('Verdana',20), bg='white')
    labelVacio.grid(row=0, column=0, pady=70, padx=10, sticky=E)

    botonAgregar = Button(frameMenuDiaFestivo, text = "Registrar Día Festivo", image = iconoAgregar, bg='white', relief='flat', command=mostrarRegistrarDiaFestivo)
    botonAgregar.grid(row=1, column=1, pady=20, padx=40)
    labelAgregar = Label(frameMenuDiaFestivo, text="Registrar Día Festivo", font=('Verdana',14), bg='white')
    labelAgregar.grid(row=2, column=1)
    botonEliminar = Button(frameMenuDiaFestivo, text = "Eliminar Día Festivo", image = iconoEliminar, bg='white', relief='flat', command=mostrarEliminarDiaFestivo)
    botonEliminar.grid(row=1, column=2, pady=20, padx=50)
    labelEliminar = Label(frameMenuDiaFestivo, text="Eliminar Día Festivo", font=('Verdana',14), bg='white')
    labelEliminar.grid(row=2, column=2)
    botonConsultar = Button(frameMenuDiaFestivo, text = "Consultar Día Festivo", image = iconoConsultar, bg='white', relief='flat', command = mostrarConsultarDiasFestivo)
    botonConsultar.grid(row=1, column=3, pady=20, padx=40)
    labelConsultar = Label(frameMenuDiaFestivo, text="Consultar Día Festivo", font=('Verdana',14), bg='white')
    labelConsultar.grid(row=2, column=3)

def mostrarMenuDiaExcepcion():
    for widget in contenedorFrames.winfo_children():
        widget.destroy()

    nombreModulo.config(text="Menú Día Excepción")
    frameMenuDiaExcepcion = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameMenuDiaExcepcion.grid(row=1, column=0, columnspan=2)
    frameMenuDiaExcepcion.grid_propagate(False)

    labelVacio = Label(frameMenuDiaExcepcion, text="", font=('Verdana',20), bg='white')
    labelVacio.grid(row=0, column=0, pady=70, padx=10, sticky=E)

    botonAgregar = Button(frameMenuDiaExcepcion, text = "Registrar Día Excepción", image = iconoAgregar, bg='white', relief='flat', command=mostrarRegistrarDiaExcepcion)
    botonAgregar.grid(row=1, column=1, pady=20, padx=40)
    labelAgregar = Label(frameMenuDiaExcepcion, text="Registrar Día Excepción", font=('Verdana',14), bg='white')
    labelAgregar.grid(row=2, column=1)
    botonEliminar = Button(frameMenuDiaExcepcion, text = "Eliminar Día Excepción", image = iconoEliminar, bg='white', relief='flat', command=mostrarEliminarDiaExcepcion)
    botonEliminar.grid(row=1, column=2, pady=20, padx=50)
    labelEliminar = Label(frameMenuDiaExcepcion, text="Eliminar Día Excepción", font=('Verdana',14), bg='white')
    labelEliminar.grid(row=2, column=2)
    botonConsultar = Button(frameMenuDiaExcepcion, text = "Consultar Día Excepción", image = iconoConsultar, bg='white', relief='flat', command = mostrarConsultarDiasExcepcion)
    botonConsultar.grid(row=1, column=3, pady=20, padx=40)
    labelConsultar = Label(frameMenuDiaExcepcion, text="Consultar Día Excepción", font=('Verdana',14), bg='white')
    labelConsultar.grid(row=2, column=3)

def mostrarIniciarSesion():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  for boton in contenedorBotones.winfo_children():
    boton.config(state="disabled")

  nombreModulo.config(text="Iniciar Sesión")
  frameLogin = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameLogin.grid(row=1, column=0, columnspan=2)
  frameLogin.grid_propagate(False)

  labelVacio = Label(frameLogin, text="", font=('Verdana',20), bg='white')
  labelVacio.grid(row=1, column=0, pady=30, sticky=E)

  labelAdmin = Label(frameLogin, text="Usuario:", font=('Verdana',20), bg='white')
  labelAdmin.grid(row=2, column=0, pady=30, padx=30, sticky=E)
  nombreAdmin= StringVar()
  textoAdmin = Entry(frameLogin, bd=5, textvariable=nombreAdmin, font=('Verdana',20))
  textoAdmin.grid(row=2, column=1, padx=5, pady=30)

  admin = Administrador()

  labelPassword = Label(frameLogin, text="Contraseña:", font=('Verdana',20), bg='white')
  labelPassword.grid(row=3, column=0, pady=30, padx=30, sticky=E)
  passwordVar= StringVar()
  textoPassword = Entry(frameLogin, bd=5, textvariable=passwordVar, font=('Verdana',20), show='*')
  textoPassword.grid(row=3, column=1, padx=5, pady=30)
  textoPassword.bind("<Return>", lambda x: admin.iniciarSesion(textoAdmin,textoPassword, botonIniciarSesion, contenedorBotones, db))

  botonIniciarSesion = Button(frameLogin, text="Iniciar Sesión", font=('Verdana',20), command=lambda: admin.iniciarSesion(textoAdmin,textoPassword, botonIniciarSesion, contenedorBotones, db)) 
  botonIniciarSesion.grid(row=6, column=0, padx=70, pady=70, sticky=W)
  
  botonContrasena = Button(frameLogin, text="Reestablecer Contraseña", font=('Verdana',20), command=mostrarReestablecerContraseña) 
  botonContrasena.grid(row=6, column=1, padx=60,pady=70, sticky=W)

def mostrarReestablecerContraseña():
  admin = Administrador()
  if admin.mandarCodigoVerificacion(db):
    messagebox.showinfo('Reestablecer Contraseña','Se ha enviado al correo electrónico un codigo de verificación.')

    for widget in contenedorFrames.winfo_children():
      widget.destroy()

    nombreModulo.config(text="Reestablecer contraseña")
    frameLogin = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
    frameLogin.grid(row=1, column=0, columnspan=2)
    frameLogin.grid_propagate(False)

    labelVacio = Label(frameLogin, text="", font=('Verdana',20), bg='white')
    labelVacio.grid(row=1, column=0, pady=30, sticky=E)
    
    labelCodigo = Label(frameLogin, text="Código de verificación:", font=('Verdana',20), bg='white')
    labelCodigo.grid(row=2, column=0, pady=30, padx=10, sticky=E)
    codigo= StringVar()
    textoCodigo = Entry(frameLogin, bd=5, textvariable=codigo, font=('Verdana',20))
    textoCodigo.grid(row=2, column=1, pady=30)

    labelPassword = Label(frameLogin, text="Contraseña nueva:", font=('Verdana',20), bg='white')
    labelPassword.grid(row=3, column=0, pady=30, padx=10, sticky=E)
    passwordVar= StringVar()
    textoPassword = Entry(frameLogin, bd=5, textvariable=passwordVar, font=('Verdana',20), show='*')
    textoPassword.grid(row=3, column=1, pady=30)
  
    labelPasswordV = Label(frameLogin, text="Verificar contraseña nueva:", font=('Verdana',20), bg='white')
    labelPasswordV.grid(row=4, column=0, pady=30, padx=10, sticky=E)
    passwordVVar= StringVar()
    textoPasswordV = Entry(frameLogin, bd=5, textvariable=passwordVVar, font=('Verdana',20), show='*')
    textoPasswordV.grid(row=4, column=1, pady=30)

    botonCambiarContraseña = Button(frameLogin, text="Cambiar contraseña", font=('Verdana',20), command=lambda: admin.cambiarContrasena(botonCambiarContraseña, textoCodigo, textoPassword, textoPasswordV, db)) 
    botonCambiarContraseña.grid(row=6, column=0, pady=80, padx=60)

    botonRegresar = Button(frameLogin, text="Regresar", font=('Verdana',20), command=mostrarIniciarSesion) 
    botonRegresar.grid(row=6, column=1, pady=70, sticky=E)
  
  else:
    messagebox.showerror("¡Error!","No fue posible mandar el correo con código de verificación. Intente más tarde.")

def mostrarAltaEmpleado():
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

  botonRegistrar = Button(frameAltaEmpleados, text="Alta Empleado", font=('Verdana',20), command=lambda: empleado.altaEmpleado(textoIdEmpleado,textoNombreEmpleado,textoApellidoP,textoApellidoM,db)) 
  botonRegistrar.grid(row=5,column=0, padx=80, pady=70, sticky=W)

  botonBorrar = Button(frameAltaEmpleados, text="Borrar Campos", font=('Verdana',20), command=lambda: empleado.borrar(textoNombreEmpleado,textoApellidoP,textoApellidoM)) 
  botonBorrar.grid(row=5,column=1, pady=70, padx=20, sticky=E)

def mostrarModificarEmpleado():
  for widget in contenedorFrames.winfo_children():
      widget.destroy()
  
  empleados = Empleado()
  nombreModulo.config(text="Modificar Empleado")
  frameModificarEmpleados = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameModificarEmpleados.grid(row=1,column=0, columnspan=2)
  frameModificarEmpleados.grid_propagate(False)

  labelIdEmpleado = Label(frameModificarEmpleados, text="Empleado:", font=('Verdana',18), bg='white')
  labelIdEmpleado.grid(row=1,column=0, pady=30, sticky=E)
  idVar= StringVar()

  valores = empleados.listar(db)
  comboEmpleados = ttk.Combobox(frameModificarEmpleados, values= valores, state="readonly", width=33, font=('Verdana',16))
  comboEmpleados.grid(row=1, column=1)
  comboEmpleados.bind("<<ComboboxSelected>>", lambda x: empleados.consultarEmpleado(comboEmpleados, textoNombreEmpleado, textoApellidoP, textoApellidoM, comboEstado, db))
  comboEmpleados.current(0)

  labelNombreEmpleado = Label(frameModificarEmpleados, text="Nombre:", font=('Verdana',18), bg='white')
  labelNombreEmpleado.grid(row=2,column=0, pady=30, sticky=E)
  nombreVar= StringVar()
  textoNombreEmpleado = Entry(frameModificarEmpleados, bd=5, textvariable=nombreVar, font=('Verdana',18), state='disabled', width =30)
  textoNombreEmpleado.grid(row=2, column=1, pady=30, sticky=W)

  labelApellidoP = Label(frameModificarEmpleados, text="Apellido Paterno:", font=('Verdana',18), bg='white')
  labelApellidoP.grid(row=3,column=0, pady=30, sticky=E)
  apellidoPVar= StringVar()
  textoApellidoP = Entry(frameModificarEmpleados, bd=5, textvariable=apellidoPVar, font=('Verdana',18), state='disabled', width=30)
  textoApellidoP.grid(row=3, column=1, pady=30, sticky=W)

  labelApellidoM = Label(frameModificarEmpleados, text="Apellido Materno:", font=('Verdana',18), bg='white')
  labelApellidoM.grid(row=4,column=0, pady=30, sticky=E)
  apellidoMVar= StringVar()
  textoApellidoM = Entry(frameModificarEmpleados, bd=5, textvariable=apellidoMVar, font=('Verdana',18), state='disabled', width=30)
  textoApellidoM.grid(row=4, column=1, pady=30, sticky=W)

  labelEstado = Label(frameModificarEmpleados, text="Estado:", font=('Verdana',18), bg='white')
  labelEstado.grid(row=5,column=0, pady=30, sticky=E)
  comboEstado= ttk.Combobox(frameModificarEmpleados, state='readonly', font=('Verdana',18), width=20)
  comboEstado['values'] = ('Activo','Baja')
  comboEstado.grid(row=5, column=1, pady=30, sticky=W)
  comboEstado.current(0)

  botonModificar = Button(frameModificarEmpleados, text="Modificar Empleado", font=('Verdana',20), command=lambda: empleados.modificarEmpleado(comboEmpleados,textoNombreEmpleado,textoApellidoP,textoApellidoM,comboEstado,db)) 
  botonModificar.grid(row=6,column=0, padx=30, pady=70)

  botonBorrar = Button(frameModificarEmpleados, text="Borrar Campos", font=('Verdana',20), command=lambda: empleado.borrarAlterno(textoIdEmpleado,textoNombreEmpleado,textoApellidoP,textoApellidoM)) 
  botonBorrar.grid(row=6,column=1, pady=70, padx=10, sticky=E)

def mostrarConsultarEmpleados():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Consultar Empleados")
  frameConsultarEmpleados = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameConsultarEmpleados.grid(row=1, column=0, columnspan=2)
  frameConsultarEmpleados.grid_propagate(False)

  tablaEmpleados= ttk.Treeview(frameConsultarEmpleados, height=25)
  tablaEmpleados["columns"] = ['0', '1']
  tablaEmpleados['show'] = 'headings'
  tablaEmpleados.grid(row=0, column=0, padx=175, pady=50)
  tablaEmpleados.column('0', anchor="center")
  tablaEmpleados.column('1', width=300, anchor="center")
  tablaEmpleados.heading('0', text="IdEmpleado", anchor="center")
  tablaEmpleados.heading('1', text="Nombre Completo", anchor="center")

  empleados= Empleado()
  listaEmpleados = empleados.listar(db)

  for empleado in listaEmpleados:
      tablaEmpleados.insert('', END, text=empleado[0], values=(empleado[0:7], empleado[8:]))

def mostrarRegistrarEmpresa():
  for widget in contenedorFrames.winfo_children():
          widget.destroy()
  
  for boton in contenedorBotones.winfo_children():
        boton.config(state="disabled")

  empresa = Empresa()
   
  nombreModulo.config(text="Registrar Empresa")
  frameRegistrarEmpresa = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameRegistrarEmpresa.grid(row=1,column=0, columnspan=2)
  frameRegistrarEmpresa.grid_propagate(False)

  labelVacio = Label(frameRegistrarEmpresa, text="", font=('Verdana',20), bg='white')
  labelVacio.grid(row=0,column=0, pady=5, sticky=E)

  labelRFC = Label(frameRegistrarEmpresa, text="RFC:", font=('Verdana',20), bg='white')
  labelRFC.grid(row=1,column=0, pady=10, sticky=E)
  RFCVar= StringVar()
  textoRFC = Entry(frameRegistrarEmpresa, bd=5, font=('Verdana',20), textvariable=RFCVar)
  textoRFC.grid(row=1, column=1, padx=5, pady=10)

  labelNombreEmpresa = Label(frameRegistrarEmpresa, text="Nombre:", font=('Verdana',20), bg='white')
  labelNombreEmpresa.grid(row=2,column=0, pady=10, sticky=E)
  nombreVar= StringVar()
  textoNombreEmpresa = Entry(frameRegistrarEmpresa, bd=5, textvariable=nombreVar, font=('Verdana',20))
  textoNombreEmpresa.grid(row=2, column=1, padx=5, pady=10)

  labelDireccion = Label(frameRegistrarEmpresa, text="Dirección:", font=('Verdana',20), bg='white')
  labelDireccion.grid(row=3,column=0, pady=10, sticky=E)
  apellidoPVar= StringVar()
  textoDireccion = Entry(frameRegistrarEmpresa, bd=5, textvariable=apellidoPVar, font=('Verdana',20))
  textoDireccion.grid(row=3, column=1, padx=5, pady=10)

  labelTelefono = Label(frameRegistrarEmpresa, text="Teléfono:", font=('Verdana',20), bg='white')
  labelTelefono.grid(row=4,column=0, pady=10, sticky=E)
  textoTelefono = Entry(frameRegistrarEmpresa, bd=5, validate='key', font=('Verdana',20))
  textoTelefono['validatecommand'] = (textoTelefono.register(validarEntrada),'%S','%P')
  textoTelefono.grid(row=4, column=1, padx=5, pady=10)

  labelEmail = Label(frameRegistrarEmpresa, text="E-mail:", font=('Verdana',20), bg='white')
  labelEmail.grid(row=5,column=0, pady=10, sticky=E)
  emailVar = StringVar()
  textoEmail = Entry(frameRegistrarEmpresa, bd=5, textvariable=emailVar, font=('Verdana',20))
  textoEmail.grid(row=5, column=1, padx=5, pady=10)

  labelContrasena = Label(frameRegistrarEmpresa, text="Contraseña:", font=('Verdana',20), bg='white')
  labelContrasena.grid(row=6,column=0, pady=10, sticky=E)
  contrasenaVar = StringVar()
  textoContrasena = Entry(frameRegistrarEmpresa, bd=5, textvariable=contrasenaVar, font=('Verdana',20))
  textoContrasena.grid(row=6, column=1, padx=5, pady=10)

  labelContrasenaV = Label(frameRegistrarEmpresa, text="Repetir contraseña:", font=('Verdana',20), bg='white')
  labelContrasenaV.grid(row=7,column=0, pady=10, sticky=E)
  contrasenaVVar = StringVar()
  textoContrasenaV = Entry(frameRegistrarEmpresa, bd=5, textvariable=contrasenaVVar, font=('Verdana',20))
  textoContrasenaV.grid(row=7, column=1, padx=20, pady=10)

  botonRegistrar = Button(frameRegistrarEmpresa, text="Registrar Empresa", font=('Verdana',20), command=lambda: empresa.registrarEmpresa(textoRFC, textoNombreEmpresa, textoDireccion, textoTelefono,textoEmail, textoContrasena, textoContrasenaV, botonRegistrar, botonIniciarSesion, db)) 
  botonRegistrar.grid(row=8,column=0, padx=50, pady=50, sticky=E)

  botonIniciarSesion = Button(frameRegistrarEmpresa, text="Iniciar Sesión", state = 'disabled', font=('Verdana',20), command=mostrarIniciarSesion ) 
  botonIniciarSesion.grid(row=8,column=1, padx=50, pady=50, sticky=E)

def mostrarConsultarEmpresa():
  for widget in contenedorFrames.winfo_children():
      widget.destroy()
  
  empresa = Empresa()

  #Consulta datos de la empresa
  rfc,nombreEmpresa,direccion,telefono,email = empresa.consultarEmpresa(db)

  nombreModulo.config(text="Consultar Empresa")
  frameConsultarEmpresa = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameConsultarEmpresa.grid(row=1,column=0, columnspan=2)
  frameConsultarEmpresa.grid_propagate(False)

  labelRFC = Label(frameConsultarEmpresa, text="RFC:", font=('Verdana',20), bg='white')
  labelRFC.grid(row=1,column=0, pady=30, padx=50, sticky=E)
  textoRFC = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
  textoRFC.insert(0,rfc)
  textoRFC.config(state = 'disabled')
  textoRFC.grid(row=1, column=1, padx=5, pady=30)
  
  labelNombreEmpresa = Label(frameConsultarEmpresa, text="Nombre Empresa:", font=('Verdana',20), bg='white')
  labelNombreEmpresa.grid(row=2,column=0, pady=30, padx=50, sticky=E)
  textoNombreEmpresa = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
  textoNombreEmpresa.insert(0,nombreEmpresa)
  textoNombreEmpresa.config(state = 'disabled')
  textoNombreEmpresa.grid(row=2, column=1, padx=5, pady=30)

  labelDireccion = Label(frameConsultarEmpresa, text="Dirección:", font=('Verdana',20), bg='white')
  labelDireccion.grid(row=3,column=0, pady=30, padx=50, sticky=E)
  textoDireccion = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
  textoDireccion.insert(0,direccion)
  textoDireccion.config(state = 'disabled')
  textoDireccion.grid(row=3, column=1, padx=5, pady=30)

  labelTelefono = Label(frameConsultarEmpresa, text="Teléfono:", font=('Verdana',20), bg='white')
  labelTelefono.grid(row=4,column=0, pady=30, padx=50, sticky=E)
  textoTelefono = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
  textoTelefono.insert(0,telefono)
  textoTelefono.config(state = 'disabled')
  textoTelefono.grid(row=4, column=1, padx=5, pady=30)

  labelEmail = Label(frameConsultarEmpresa, text="Email:", font=('Verdana',20), bg='white')
  labelEmail.grid(row=5,column=0, pady=30, padx=50, sticky=E)
  textoEmail = Entry(frameConsultarEmpresa, bd=5, font=('Verdana',20))
  textoEmail.insert(0,email)
  textoEmail.config(state = 'disabled')
  textoEmail.grid(row=5, column=1, padx=5, pady=30)

def mostrarRegistrarDiaFestivo():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Registrar Día Festivo")
  frameRegistrarDiaFeriado = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameRegistrarDiaFeriado.grid(row=1, column=0, columnspan=2)
  frameRegistrarDiaFeriado.grid_propagate(False)

  labelVacio = Label(frameRegistrarDiaFeriado, text=" ", font=('Verdana',20), bg='white')
  labelVacio.grid(row=1, column=0, pady=30)

  labelFecha = Label(frameRegistrarDiaFeriado, text="Nuevo día festivo:", font=('Verdana',20), bg='white')
  labelFecha.grid(row=1, column=1, pady=30)

  calendario = Calendar(frameRegistrarDiaFeriado, selectmode = 'day', locale='es_MX')
  calendario.grid(row=2, column=1, pady=30)

  diaFestivo = DiaFestivo()

  botonRegistrarDiaFestivo = Button(frameRegistrarDiaFeriado, text="Registrar día", font=('Verdana',20), command=lambda: diaFestivo.registrarDiaFestivo(calendario,db)) 
  botonRegistrarDiaFestivo.grid(row=6, column=1, padx=300, pady=70)

def mostrarRegistrarDiaExcepcion():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Registrar Día Excepción")
  frameRegistrarDiaExcepcion = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameRegistrarDiaExcepcion.grid(row=1, column=0, columnspan=2)
  frameRegistrarDiaExcepcion.grid_propagate(False)

  diaExcepcion = DiaExcepcion()
  empleado = Empleado()
  valores = empleado.listar(db)

  labelEmpleados = Label(frameRegistrarDiaExcepcion, text="Empleado:", font=('Verdana',20), bg='white')
  labelEmpleados.grid(row=1, column=1, pady=40, padx=20)

  comboEmpleados = ttk.Combobox(frameRegistrarDiaExcepcion, values= valores, state="readonly", width=40, font=('Verdana',18))
  comboEmpleados.grid(row=1, column=2)
  comboEmpleados.current(0)

  labelFecha = Label(frameRegistrarDiaExcepcion, text="Nuevo día Excepción:", font=('Verdana',20), bg='white')
  labelFecha.grid(row=3, column=1, columnspan = 2, pady=30)

  calendario = Calendar(frameRegistrarDiaExcepcion, selectmode = 'day', locale='es_MX')
  calendario.grid(row=4, column=1, columnspan = 2, pady=30)

  botonRegistrarDiaExcepcion= Button(frameRegistrarDiaExcepcion, text="Registrar día", font=('Verdana',20), command=lambda: diaExcepcion.registrarDiaExcepcion(comboEmpleados,calendario,db)) 
  botonRegistrarDiaExcepcion.grid(row=6, column=1, columnspan=2, padx=50, pady=70)

def mostrarConsultarDiasFestivo():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Consultar Dias Festivos")
  frameConsultarDiasFestivo = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameConsultarDiasFestivo.grid(row=1, column=0, columnspan=2)
  frameConsultarDiasFestivo.grid_propagate(False)

  tablaDiasFestivos= ttk.Treeview(frameConsultarDiasFestivo, height=25)
  tablaDiasFestivos["columns"] = ['0', '1']
  tablaDiasFestivos['show'] = 'headings'
  tablaDiasFestivos.grid(row=0, column=0, padx=175, pady=50)
  tablaDiasFestivos.column('0', anchor="center")
  tablaDiasFestivos.column('1', width=300, anchor="center")
  tablaDiasFestivos.heading('0', text="Registro", anchor="center")
  tablaDiasFestivos.heading('1', text="Fecha", anchor="center")

  diaFestivo = DiaFestivo()
  dias = diaFestivo.listarDiasFestivos(db)

  for dia in dias:
      tablaDiasFestivos.insert('', END, text=dia[0], values=(dia[0],"{} {} de {} de {}".format(dia[1], str(dia[2]), dia[3], str(dia[4]))))

def mostrarConsultarDiasExcepcion():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Consultar Dias de Excepción")
  frameConsultarDiasExcepcion = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameConsultarDiasExcepcion.grid(row=1, column=0, columnspan=2)
  frameConsultarDiasExcepcion.grid_propagate(False)
  
  diaExcepcion = DiaExcepcion()
  empleado = Empleado()
  valores = empleado.listar(db)

  labelEmpleados = Label(frameConsultarDiasExcepcion, text="Empleado:", font=('Verdana',20), bg='white')
  labelEmpleados.grid(row=1, column=0, pady=40, padx=20)

  comboEmpleados = ttk.Combobox(frameConsultarDiasExcepcion, values= valores, state="readonly", width=40, font=('Verdana',18))
  comboEmpleados.grid(row=1, column=1)
  comboEmpleados.bind("<<ComboboxSelected>>", lambda x: diaExcepcion.listarDiasExcepcion(tablaDiasExcepcion, comboEmpleados, db))
  comboEmpleados.current(0)

  tablaDiasExcepcion= ttk.Treeview(frameConsultarDiasExcepcion, height=20)
  tablaDiasExcepcion["columns"] = ['0', '1']
  tablaDiasExcepcion['show'] = 'headings'
  tablaDiasExcepcion.grid(row=2, column=0, columnspan=2,padx=100, pady=10)
  tablaDiasExcepcion.column('0', anchor="center")
  tablaDiasExcepcion.column('1', width=300, anchor="center")
  tablaDiasExcepcion.heading('0', text="Registro", anchor="center")
  tablaDiasExcepcion.heading('1', text="Fecha", anchor="center")

def mostrarEliminarDiaFestivo():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Eliminar Dia Festivos")
  frameEliminarDiaFestivo = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameEliminarDiaFestivo.grid(row=1, column=0, columnspan=2)
  frameEliminarDiaFestivo.grid_propagate(False)

  tablaDiasFestivo= ttk.Treeview(frameEliminarDiaFestivo, height=25)
  tablaDiasFestivo["columns"] = ['0', '1']
  tablaDiasFestivo['show'] = 'headings'
  tablaDiasFestivo.grid(row=0, column=0, padx=175, pady=40)
  tablaDiasFestivo.column('0', anchor="center")
  tablaDiasFestivo.column('1', width=300, anchor="center")
  tablaDiasFestivo.heading('0', text="Registro", anchor="center")
  tablaDiasFestivo.heading('1', text="Fecha", anchor="center")

  botonEliminarDiaFestivo = Button(frameEliminarDiaFestivo, text="Eliminar día", font=('Verdana',20), command=lambda: diaFestivo.eliminarDiaFestivo(tablaDiasFestivo,db)) 
  botonEliminarDiaFestivo.grid(row=1, column=0, padx=300)

  diaFestivo = DiaFestivo()
  dias = diaFestivo.listarDiasFestivos(db)

  for dia in dias:
      tablaDiasFestivo.insert('', END, text=dia[0], values=(dia[0],"{} {} de {} de {}".format(dia[1], str(dia[2]), dia[3], str(dia[4]))))

def mostrarEliminarDiaExcepcion():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Eliminar Dias de Excepción")
  frameEliminarDiaExcepcion = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameEliminarDiaExcepcion.grid(row=1, column=0, columnspan=2)
  frameEliminarDiaExcepcion.grid_propagate(False)
  
  diaExcepcion = DiaExcepcion()
  empleado = Empleado()
  valores = empleado.listar(db)

  labelEmpleados = Label(frameEliminarDiaExcepcion, text="Empleado:", font=('Verdana',20), bg='white')
  labelEmpleados.grid(row=1, column=0, pady=40, padx=20)

  comboEmpleados = ttk.Combobox(frameEliminarDiaExcepcion, values= valores, state="readonly", width=40, font=('Verdana',18))
  comboEmpleados.grid(row=1, column=1)
  comboEmpleados.bind("<<ComboboxSelected>>", lambda x: diaExcepcion.listarDiasExcepcion(tablaDiasExcepcion, comboEmpleados, db))
  comboEmpleados.current(0)

  tablaDiasExcepcion= ttk.Treeview(frameEliminarDiaExcepcion, height=20)
  tablaDiasExcepcion["columns"] = ['0', '1']
  tablaDiasExcepcion['show'] = 'headings'
  tablaDiasExcepcion.grid(row=2, column=0, columnspan=2,padx=100, pady=10)
  tablaDiasExcepcion.column('0', anchor="center")
  tablaDiasExcepcion.column('1', width=300, anchor="center")
  tablaDiasExcepcion.heading('0', text="Registro", anchor="center")
  tablaDiasExcepcion.heading('1', text="Fecha", anchor="center")

  botonEliminarDiaFestivo = Button(frameEliminarDiaExcepcion, text="Eliminar día", font=('Verdana',20), command=lambda: diaExcepcion.eliminarDiaExcepcion(comboEmpleados,tablaDiasExcepcion,db)) 
  botonEliminarDiaFestivo.grid(row=3, column=0, columnspan=2, padx=300, pady=30)

def mostrarRegistrarHorarios():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Registrar Horarios")
  frameRegistrarHorario = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameRegistrarHorario.grid(row=1, column=0, columnspan=2)
  frameRegistrarHorario.grid_propagate(False)
  
  empleado = Empleado()
  valores = empleado.listar(db)

  labelEmpleados = Label(frameRegistrarHorario, text="Empleado:", font=('Verdana',18), bg='white')
  labelEmpleados.grid(row=1, column=0, pady=40)

  comboEmpleados = ttk.Combobox(frameRegistrarHorario, values= valores, state="readonly", width=40, font=('Verdana',16))
  comboEmpleados.grid(row=1, column=1,columnspan=2)
  comboEmpleados.current(0)

  labelDia = Label(frameRegistrarHorario, text="Dia:", font=('Verdana',18), bg='white')
  labelDia.grid(row=2, column=0, pady=20)

  comboDia = ttk.Combobox(frameRegistrarHorario, values= ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'), state="readonly", font=('Verdana',15), width=9)
  comboDia.grid(row=3, column=0)
  comboDia.current(0)

  labelHoraInicio = Label(frameRegistrarHorario, text="Hora Inicio:", font=('Verdana',18), bg='white')
  labelHoraInicio.grid(row=2, column=1, pady=20)

  valores = list()

  for i in range (0,10):
    valores.append("0{}:00".format(i))

  for i in range (10,24):
    valores.append("{}:00".format(i))

  comboHoraInicio = ttk.Combobox(frameRegistrarHorario, values=valores, state="readonly", font=('Verdana',15), width=9)
  comboHoraInicio.grid(row=3, column=1)
  comboHoraInicio.current(0)

  labelHoraFin = Label(frameRegistrarHorario, text="Hora Fin:", font=('Verdana',20), bg='white')
  labelHoraFin.grid(row=2, column=2, pady=20)

  comboHoraFin = ttk.Combobox(frameRegistrarHorario, values=valores, state="readonly", font=('Verdana',15), width=9)
  comboHoraFin.grid(row=3, column=2)
  comboHoraFin.current(0)

  horario = Horario()

  lista = list()

  botonAgregarHorarios = Button(frameRegistrarHorario, text="Agregar Horario", font=('Verdana',18), command=lambda: horario.agregarTabla(comboDia, comboHoraInicio, comboHoraFin, tablaHorario)) 
  botonAgregarHorarios.grid(row=4, column=0, columnspan=3, padx=300, pady=30)

  tablaHorario= ttk.Treeview(frameRegistrarHorario, height=5)
  tablaHorario["columns"] = ['0', '1', '2']
  tablaHorario['show'] = 'headings'
  tablaHorario.grid(row=5, column=0, columnspan=3,padx=10, pady=10)
  tablaHorario.column('0', anchor="center")
  tablaHorario.column('1', anchor="center")
  tablaHorario.column('2', anchor="center")
  tablaHorario.heading('0', text="Dia", anchor="center")
  tablaHorario.heading('1', text="Hora Entrada", anchor="center")
  tablaHorario.heading('2', text="Hora Salida", anchor="center")

  botonEliminarTabla = Button(frameRegistrarHorario, text="Eliminar fila", font=('Verdana',18), command=lambda: horario.eliminarTabla(tablaHorario)) 
  botonEliminarTabla.grid(row=6, column=0, pady=30)

  botonRegistrarHorarios = Button(frameRegistrarHorario, text="Registrar Horario", font=('Verdana',18), command=lambda: horario.registrarHorario(comboEmpleados, comboDia, comboHoraInicio, comboHoraFin, tablaHorario, db)) 
  botonRegistrarHorarios.grid(row=6, column=1, pady=30)

  botonBorrarTabla = Button(frameRegistrarHorario, text="Borrar todo", font=('Verdana',18), command=lambda: horario.borrarTabla(tablaHorario)) 
  botonBorrarTabla.grid(row=6, column=2, pady=30)

def mostrarConsultarHorarios():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Consultar Horario")
  frameConsultarHorario = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameConsultarHorario.grid(row=1, column=0, columnspan=2)
  frameConsultarHorario.grid_propagate(False)
  
  horario = Horario()
  empleado = Empleado()
  valores = empleado.listar(db)

  labelEmpleados = Label(frameConsultarHorario, text="Empleado:", font=('Verdana',18), bg='white')
  labelEmpleados.grid(row=1, column=0, pady=40, padx=10)

  comboEmpleados = ttk.Combobox(frameConsultarHorario, values= valores, state="readonly", width=40, font=('Verdana',18))
  comboEmpleados.grid(row=1, column=1,columnspan=2)
  comboEmpleados.bind("<<ComboboxSelected>>", lambda x: horario.listarHorario( comboEmpleados, tablaHorario, db))
  comboEmpleados.current(0)

  tablaHorario= ttk.Treeview(frameConsultarHorario, height=20)
  tablaHorario["columns"] = ['0', '1', '2']
  tablaHorario['show'] = 'headings'
  tablaHorario.grid(row=2, column=0, columnspan=2,padx=120, pady=10)
  tablaHorario.column('0', anchor="center")
  tablaHorario.column('1', anchor="center")
  tablaHorario.column('2', anchor="center")
  tablaHorario.heading('0', text="Día", anchor="center")
  tablaHorario.heading('1', text="Hora Entrada", anchor="center")
  tablaHorario.heading('2', text="Hora Salida", anchor="center")

def mostrarEliminarHorarios():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Eliminar Horario")
  frameEliminarHorario = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameEliminarHorario.grid(row=1, column=0, columnspan=2)
  frameEliminarHorario.grid_propagate(False)
  
  horario = Horario()
  empleado = Empleado()
  valores = empleado.listar(db)

  labelEmpleados = Label(frameEliminarHorario, text="Empleado:", font=('Verdana',18), bg='white')
  labelEmpleados.grid(row=1, column=0, pady=40)

  comboEmpleados = ttk.Combobox(frameEliminarHorario, values= valores, state="readonly", width=40, font=('Verdana',18))
  comboEmpleados.grid(row=1, column=1)
  comboEmpleados.bind("<<ComboboxSelected>>", lambda x: horario.listarHorario( comboEmpleados, tablaHorario, db))
  comboEmpleados.current(0)

  tablaHorario= ttk.Treeview(frameEliminarHorario, height=20)
  tablaHorario["columns"] = ['0', '1', '2']
  tablaHorario['show'] = 'headings'
  tablaHorario.grid(row=2, column=0, columnspan=2,padx=120, pady=10)
  tablaHorario.column('0', anchor="center")
  tablaHorario.column('1', anchor="center")
  tablaHorario.column('2', anchor="center")
  tablaHorario.heading('0', text="Día", anchor="center")
  tablaHorario.heading('1', text="Hora Entrada", anchor="center")
  tablaHorario.heading('2', text="Hora Salida", anchor="center")

  botonEliminarHorario = Button(frameEliminarHorario, text="Eliminar Horario", font=('Verdana',20), command=lambda: horario.eliminarHorario(comboEmpleados, tablaHorario, db)) 
  botonEliminarHorario.grid(row=3, column=0, columnspan=2, padx=300, pady=20, sticky=W)

def mostrarGenerarReporte():
  for widget in contenedorFrames.winfo_children():
    widget.destroy()

  nombreModulo.config(text="Generar Reporte")
  frameGenerarReporte = Frame(contenedorFrames, width=850, height=700, bd=5, bg='white', relief='ridge')
  frameGenerarReporte.grid(row=1, column=0, columnspan=2)
  frameGenerarReporte.grid_propagate(False)

  empleado = Empleado()
  reporte = Reporte()
  valores = empleado.listar(db)

  labelVacio = Label(frameGenerarReporte, text="", font=('Verdana',18), bg='white')
  labelVacio.grid(row=0, column=0, pady=5)

  labelEmpleados = Label(frameGenerarReporte, text="Empleado:", font=('Verdana',18), bg='white')
  labelEmpleados.grid(row=3, column=0, pady=20)

  comboEmpleados = ttk.Combobox(frameGenerarReporte, values= valores, state="readonly", width=40, font=('Verdana',16))
  comboEmpleados.grid(row=3, column=1)
  comboEmpleados.bind("<<ComboboxSelected>>", lambda x: reporte.llenarTabla(tablaReporte,comboEmpleados,fechaInicio,fechaFin,db))
  comboEmpleados.current(0)

  labelInicio = Label(frameGenerarReporte, text="Fecha Inicio", font=('Verdana',18), bg='white')
  labelInicio.grid(row=1, column=0)
  fechaInicio = DateEntry(frameGenerarReporte, font=('Verdana',16), locale='es_MX')
  fechaInicio.grid(row=2, column=0, padx=10)

  labelFin = Label(frameGenerarReporte, text="Fecha Fin", font=('Verdana',18), bg='white')
  labelFin.grid(row=1, column=1)
  fechaFin = DateEntry(frameGenerarReporte, font=('Verdana',16), locale='es_MX')
  fechaFin.grid(row=2, column=1)

  tablaReporte= ttk.Treeview(frameGenerarReporte, height=15)
  tablaReporte["columns"] = ['0', '1','2','3']
  tablaReporte['show'] = 'headings'
  tablaReporte.grid(row=4, column=0, columnspan=2,padx=15, pady=10)
  tablaReporte.column('0', anchor="center")
  tablaReporte.column('1', anchor="center")
  tablaReporte.column('2', anchor="center")
  tablaReporte.column('3', anchor="center")
  tablaReporte.heading('0', text="Fecha", anchor="center")
  tablaReporte.heading('1', text="Hora Entrada", anchor="center")
  tablaReporte.heading('2', text="Hora Salida", anchor="center")
  tablaReporte.heading('3', text="Horas Efectivas", anchor="center")

  botonExportarReporte = Button(frameGenerarReporte, text="Exportar Reporte", font=('Verdana',18),command=lambda: reporte.exportarCSV(comboEmpleados,fechaInicio,fechaFin,db)) 
  botonExportarReporte.grid(row=5, column=0, columnspan=2, pady=20)

#Conexión a la base de datos 
server = SSHTunnelForwarder(("198.54.125.222", 21098),
                              ssh_host_key=None,
                              ssh_username="axclzgpy",
                              ssh_password="30dpr3538T@#alex",
                              remote_bind_address=("127.0.0.1", 3306))

server.start()

try:
    db=mysql.connector.connect(user='axclzgpy_sputnik',
                     password='jU0x3CV}Dv;c@wg67L',
                     host="127.0.0.1",
                     port=server.local_bind_port, 
                     database='axclzgpy_sputnik-VII')
    print("Conexión exitosa.")
    
except Exception as e:
    messagebox.showerror("Conexión a la base de datos", "No se pudo conectar a la base de datos. " + str(e))

ventanaPrincipal = Tk()
ventanaPrincipal.title("Gestión Sputnik v1.0")
ventanaAncho = ventanaPrincipal.winfo_reqwidth()
ventanaLargo = ventanaPrincipal.winfo_reqheight()
posicionDerecha = int(ventanaPrincipal.winfo_screenwidth()/2 - ventanaAncho/0.4)
posicionAbajo = int(ventanaPrincipal.winfo_screenheight()/2 - ventanaLargo/0.45)
ventanaPrincipal.geometry("1000x800+{}+{}".format(posicionDerecha, posicionAbajo))
ventanaPrincipal.resizable(0,0)

contenedorBotones = Frame(ventanaPrincipal, width=100, height=800, bg='white')
contenedorBotones.grid(row=0, column=0, rowspan=5, pady=20, padx=10)

nombreModulo = Label(ventanaPrincipal, text="Iniciar Sesión", font=('Verdana',16), bg='white')
nombreModulo.grid(row=0, column=1, sticky='SW', pady=5)

contenedorFrames = Frame(ventanaPrincipal, width=900, height=800, bg='white')
contenedorFrames.grid(row=1, column=1, rowspan=4, columnspan=2)

iconoReporte = PhotoImage(file = ".iconos/file.png").subsample(7,7)
iconoEmpresa = PhotoImage(file = ".iconos/empresa.png").subsample(7,7)
iconoEmpleado = PhotoImage(file = ".iconos/empleados.png").subsample(7,7)
iconoHorario = PhotoImage(file = ".iconos/horario.png").subsample(7,7)
iconoFestivo = PhotoImage(file = ".iconos/festivo.png").subsample(7,7)
iconoExcepcion = PhotoImage(file = ".iconos/excepcion.png").subsample(7,7)
iconoCerrar = PhotoImage(file = ".iconos/cerrar.png").subsample(7,7)
iconoAgregar = PhotoImage(file = ".iconos/agregar.png").subsample(3,3)
iconoEliminar = PhotoImage(file = ".iconos/eliminar.png").subsample(3,3)
iconoModificar = PhotoImage(file = ".iconos/modificar.png").subsample(3,3)
iconoConsultar = PhotoImage(file = ".iconos/consultar.png").subsample(3,3)

botonEmpleado = Button(contenedorBotones, text = "Empleado", image = iconoEmpleado, bg='white', relief='flat', command=mostrarMenuEmpleado)
botonEmpleado.grid(row=0, column=0, padx=10, pady=12)
botonHorario = Button(contenedorBotones, text = "Horario", image = iconoHorario, bg='white', relief='flat', command=mostrarMenuHorario)
botonHorario.grid(row=1, column=0, padx=10, pady=12)
botonDiaF = Button(contenedorBotones, text = "Día Festivo", image = iconoFestivo, bg='white', relief='flat', command=mostrarMenuDiaFestivo)
botonDiaF.grid(row=2, column=0, padx=10, pady=12)
botonDiaE = Button(contenedorBotones, text = "Dia Excepción", image = iconoExcepcion, bg='white', relief='flat', command=mostrarMenuDiaExcepcion)
botonDiaE.grid(row=3, column=0, padx=10, pady=12)
botonEmpresa = Button(contenedorBotones, text = "Reporte", image = iconoEmpresa, bg='white', relief='flat', command=mostrarConsultarEmpresa)
botonEmpresa.grid(row=4, column=0, padx=10, pady=12)
botonReporte = Button(contenedorBotones, text = "Empresa", image = iconoReporte, bg='white', relief='flat', command=mostrarGenerarReporte)
botonReporte.grid(row=5, column=0, padx=10, pady=12)
botonCerrar = Button(contenedorBotones, text = "Cerrar", image = iconoCerrar, bg='white', relief='flat', command=cerrarSesion)
botonCerrar.grid(row=6, column=0, padx=10, pady=12)

ventanaPrincipal.config(cursor="arrow")
ventanaPrincipal.config(bg="white")

comandos = db.cursor()
comandos.execute("SELECT * FROM Empresa")
resultado = comandos.fetchone()

if resultado:
    mostrarIniciarSesion()
else:
    mostrarRegistrarEmpresa()

ventanaPrincipal.mainloop()

db.close()
server.stop()