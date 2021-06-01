from tkinter import messagebox

class Empresa():
    def registrarEmpresa(self, rfc, nombre, direccion, telefono, email, contrasena, contrasenaV, botonRegistrar, botonIniciar, db):
        #Verifica que los campos esten llenos
        if (not nombre.get()) or (not direccion.get()) or (not telefono.get()) or (not email.get()) or (not contrasena.get()) or (not contrasenaV.get()) and (not contrasena.get()==contrasena.get()):
            messagebox.showerror('¡Error!','Favor de llenar todos los campos correctamente.')
        else:
            try:
                comandos = db.cursor()
        
                mensaje = messagebox.askquestion('Registar Empresa','¿Estás seguro que la información es correcta?')
            
                if mensaje == 'yes':
                    query = 'INSERT INTO Empresa (rfc,nombreEmpresa,direccion,telefono,email,contrasena) VALUES ("{}","{}","{}","{}","{}","{}")'.format(rfc.get(),nombre.get(),direccion.get(),telefono.get(),email.get(),contrasena.get())
                    comandos.execute(query)
                    rfc.config(state='disabled')
                    nombre.config(state='disabled')
                    direccion.config(state='disabled')
                    telefono.config(state='disabled')
                    email.config(state='disabled')
                    contrasena.config(state='disabled')
                    contrasenaV.config(state='disabled')
                    botonRegistrar.config(state='disabled')
                    botonIniciar.config(state='normal')

                    messagebox.showinfo('Registrar Empresa','Empresa registrada con éxito.')
            except Exception as e:
                messagebox.showerror('¡Error!','No se pudo registrar la empresa. ' + str(e))

    def consultarEmpresa(self, db):
        try: 
            comandos = db.cursor()
            comandos.execute('SELECT rfc, nombreEmpresa, direccion, telefono, email from Empresa')
            resultado = comandos.fetchone()
            return resultado
        except Exception as e:
            messagebox.showerror('¡Error!','No se pudo consultar la información de la empresa.' + str(e))
