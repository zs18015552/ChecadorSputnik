from tkinter import *
from tkinter import messagebox
from email.message import EmailMessage
import smtplib
import random 


class Administrador():

    def iniciarSesion(self, admin, password, boton, contenedorBotones, db):
        if (not admin.get()) or (not password.get()):
            messagebox.showerror('¡Error!','Favor de llenar todos los campos.')
        
        else:
            try:
                comandos = db.cursor()

                query = "SELECT email, contrasena from Empresa"
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
                    messagebox.showerror('¡Error!','Usuario y/o contraseña inválidos.')
            except Exception as e:
                messagebox.showerror('¡Error!','No fue posible hacer la autentificación. ' + str(e))

    def mandarCodigoVerificacion(self, db):
        numeroVerificacion = random.randint(1000,9999)
    
        correo = EmailMessage()
        correo.set_content(f"Su código de verificación para restablecer contraseña es: {numeroVerificacion} \n\n---\nEquipo de Soporte Sputnik VI.")

        comandos = db.cursor()
        query="SELECT email FROM Empresa"
        comandos.execute(query)
        resultado = comandos.fetchone()
        receptor = resultado[0]

        query="SELECT correo, psswd from Sputnik"
        comandos.execute(query)
        resultado = comandos.fetchone()
        emisor = resultado[0]
        password = resultado[1]

        query='UPDATE Sputnik SET codigo={} WHERE correo="{}"'.format(numeroVerificacion,emisor)
        comandos.execute(query)
        db.commit()

        correo['Subject'] = 'Código de Verificación para reestablecer contraseña.'
        correo['From'] = emisor
        correo['To'] = receptor

        server = smtplib.SMTP_SSL('sputnik.axcl.page',465)
        server.ehlo()
        server.login(emisor, password)
        print("Conexion Exitosa")
        server.send_message(correo)
        server.quit()

        return True

    def cambiarContrasena(self, boton, codigo, contrasena, verificacion, db):
        if (not contrasena.get()) or (not verificacion.get()) or (not contrasena.get()):
            messagebox.showerror('¡Error!','Favor de llenar todos los campos.')

        else:
            if not contrasena.get()==verificacion.get():
                messagebox.showerror('¡Error!','Las contraseñas no coinciden en los campos.')

            else:
                comandos = db.cursor()
                query = 'SELECT codigo from Sputnik'
                comandos.execute(query)
                resultado = comandos.fetchone()

                codigoBD = resultado[0]

                if not codigo.get()==str(codigoBD):
                    messagebox.showerror("¡Error!","Codigo de verificación incorrecto.")

                else:
                    try:
                        query = 'UPDATE Empresa SET contrasena = "{}"'.format(contrasena.get())
                        comandos.execute(query)
                        db.commit()

                        messagebox.showinfo("Cambiar Contraseña", "Contraseña cambiada con éxito")

                        for widget in contenedorFrames.winfo_children():
                            widget.config(state='disabled')

                    except Exception as e:
                        messagebox.showerror('¡Error!','No fue posible hacer el cambio de contraseña. ' + str(e))
