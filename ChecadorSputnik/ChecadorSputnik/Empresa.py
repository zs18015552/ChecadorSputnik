from tkinter import *
from tkinter import messagebox

class Empresa():
    def registrarEmpresa(self, rfc, nombre, direccion, telefono, email,boton, db):
        #Verifica que los campos esten llenos
        if (not nombre.get()) or (not direccion.get()) or (not telefono.get()) or (not email.get()):
            mensaje = messagebox.showerror('¡Error!','Favor de llenar todos los campos.')
        else:     
            comandos = db.cursor()
        
            mensaje = messagebox.askquestion('Registar Empresa','¿Estás seguro que la información es correcta?')
            
            if mensaje == 'yes':
                query = 'INSERT INTO Empresa (rfc,nombreEmpresa,direccion,telefono,email) VALUES ("{}","{}","{}","{}","{}")'.format(rfc.get(),nombre.get(),direccion.get(),telefono.get(),email.get())
                comandos.execute(query)
                rfc.config(state='disabled')
                nombre.config(state='disabled')
                direccion.config(state='disabled')
                telefono.config(state='disabled')
                email.config(state='disabled')
                boton.config(state='disabled')

    def consultarEmpresa(self, db):
        comandos = db.cursor()
        comandos.execute('SELECT * from Empresa')
        resultado = comandos.fetchone()
        return resultado
