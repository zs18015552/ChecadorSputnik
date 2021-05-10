from tkinter import *
from tkinter import messagebox

class Administrador():

    def iniciarSesion(self, admin, password, boton, contenedorBotones, db):
        if (not admin.get()) or (not password.get()):
            mensaje = messagebox.showerror('¡Error!','Favor de llenar todos los campos.')
        
        else:
            try:
                comandos = db.cursor()

                query = "SELECT nombreEmpresa, telefono from Empresa"
                comandos.execute(query)
                resultado = comandos.fetchone()

                if resultado[0]==admin.get() and resultado[1]==password.get():
                    mensaje = messagebox.showinfo('Inicio de sesión','Se inició sesión con éxito.')
                    admin.config(text="", textvariable="", state='disabled')
                    password.config(text="", state='disabled')
                    boton.config(state='disabled')

                    for boton in contenedorBotones.winfo_children():
                        boton.config(state="normal")
                else:
                    mensaje = messagebox.showerror('¡Error!','Usuario y/o contraseña inválidos.')
            except Exception as e:
                    mensaje = messagebox.showerror('¡Error!','No fue posible hacer la autentificación.')
