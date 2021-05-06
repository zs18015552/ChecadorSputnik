from tkinter import *
from tkinter import messagebox

class Administrador():

    def iniciarSesion(self, admin, password, db):
        if (not admin) or (not password):
            mensaje = messagebox.showerror('¡Error!','Favor de llenar todos los campos.')
        
        else:
            comandos = db.cursor()

            query = "SELECT nombreEmpresa, telefono from Empresa"
            comandos.execute(query)
            resultado = comandos.fetchone()

            if resultado[0]==admin and resultado[1]==password:
                return True
            else:
                return False
