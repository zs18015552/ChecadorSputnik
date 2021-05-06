from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

class Empleado():
    def listar(self,db):
        try:
            comandos = db.cursor()
            comandos.execute("SELECT idEmpleado, CONCAT_WS(' ',nombre,apellidoPaterno,apellidoMaterno) AS nombreCompleto FROM Empleados WHERE estado=1 ORDER BY IdEmpleado")
            registros = comandos.fetchall()
            valores = list()
            for dia in registros:
                valores.append(str(dia[0]) + "-" + dia[1])

            return valores

        except Exception as e:
            print(e)
            mensaje = messagebox.showerror('Día Excepcion','Error al acceder a la base de datos.')

    def consultarEmpleado(self, idEmpleado, nombre, apellidoP, apellidoM, db):
        #Consulta si el empleado existe
        try:
            comandos = db.cursor()
            query = "SELECT nombre, apellidoPaterno, apellidoMaterno from Empleados WHERE idEmpleado = {} AND estado = 1".format(idEmpleado.get())
            comandos.execute(query)
            resultado = comandos.fetchone()

            if resultado:
                nombre.config(state='normal')
                apellidoP.config(state='normal')
                apellidoM.config(state='normal')
                nombre.delete(0,END)
                apellidoP.delete(0,END)
                apellidoM.delete(0,END)
                nombre.insert(0,resultado[0])
                apellidoP.insert(0,resultado[1])
                apellidoM.insert(0,resultado[2])
                nombre.config(state='disabled')
                apellidoP.config(state='disabled')
                apellidoM.config(state='disabled')

            else:
                mensaje = messagebox.showerror('¡Error!','Empleado no encontrado.')
        except Exception as e:
            mensaje = messagebox.showerror('¡Error!','No se pudo acceder a la base de datos.')

    def consultarEmpleadoAlterno(self, idEmpleado, nombre, apellidoP, apellidoM, estado, db):
        try:
            comandos = db.cursor()
            query = "SELECT nombre, apellidoPaterno, apellidoMaterno, estado FROM Empleados WHERE idEmpleado = {}".format(idEmpleado.get())
            comandos.execute(query)
            resultado = comandos.fetchone()

            if resultado:
                nombre.config(state='normal')
                apellidoP.config(state='normal')
                apellidoM.config(state='normal')
                nombre.delete(0,END)
                apellidoP.delete(0,END)
                apellidoM.delete(0,END)
                nombre.insert(0,resultado[0])
                apellidoP.insert(0,resultado[1])
                apellidoM.insert(0,resultado[2])
                estado.current((0 if resultado[3]==1 else 1))
                idEmpleado.config(state='disabled')

            else:
                mensaje = messagebox.showerror('¡Error!','Empleado no encontrado.')
        except Exception as e:
            mensaje = messagebox.showerror('¡Error!','No se pudo acceder a la base de datos.')

    def borrar(self, nombre, apellidoP, apellidoM):
        nombre.delete(0, END)
        apellidoP.delete(0, END)
        apellidoM.delete(0, END)
        nombre.focus()

    def borrarAlterno(self, idEmpleado, nombre, apellidoP, apellidoM):
        nombre.config(state='normal')
        apellidoP.config(state='normal')
        apellidoM.config(state='normal')
        idEmpleado.config(state='normal')
        nombre.delete(0, END)
        apellidoP.delete(0, END)
        apellidoM.delete(0, END)
        idEmpleado.delete(0, END)
        nombre.config(state='disabled')
        apellidoP.config(state='disabled')
        apellidoM.config(state='disabled')
        idEmpleado.focus()

    def altaEmpleado(self, idEmpleado, nombre,apellidoP, apellidoM, db):
        #Verifica que todos los campos este llenos
        if (not nombre.get()) or (not apellidoP.get()) or (not apellidoM.get()):
            mensaje = messagebox.showerror('¡Error!','Favor de llenar todos los campos.')
        else:
            try:
                comandos = db.cursor()
        
                mensaje = messagebox.askquestion('Registar Empleado','¿Estás seguro que la información es correcta?')
            
                if mensaje == 'yes':
                    query = 'INSERT INTO Empleados (nombre,apellidoPaterno,apellidoMaterno) VALUES ("{}","{}","{}")'.format(nombre.get(),apellidoP.get(),apellidoM.get())
                    comandos.execute(query)
                    db.commit()
                    self.borrar(nombre,apellidoP,apellidoM)
                    idEmpleado.config(state='normal')
                    id = int(idEmpleado.get()) + 1
                    idEmpleado.delete(0,END)
                    idEmpleado.insert(0,id)
                    idEmpleado.config(state='disabled')
            except Exception as e:
                mensaje = messagebox.showerror('¡Error!','No se pudo acceder a la base de datos.')
    
    def bajaEmpleado(self, idEmpleado, nombre, apellidoP, apellidoM, db):
        #Verifica que el campo de idEmpleado este lleno
        if (not idEmpleado.get()):
            mensaje = messagebox.showerror('¡Error!','Favor de llenar el campo.')
        else:
            try:
                comandos = db.cursor()
        
                mensaje = messagebox.askquestion('Baja Empleado','¿Estás seguro de continuar con la operación?')
            
                if mensaje == 'yes':
                    query = 'UPDATE Empleados SET estado = 0 WHERE idEmpleado = {}'.format(idEmpleado.get())
                    comandos.execute(query)
                    db.commit()
                    self.borrarAlterno(idEmpleado,nombre,apellidoP,apellidoM)
            except Exception as e:
                mensaje = messagebox.showerror('¡Error!','No se pudo acceder a la base de datos.')

    def modificarEmpleado(self, idEmpleado, nombre, apellidoP, apellidoM, estado, db):
        #Verifica que los campos esten llenos y modifica
        if (not nombre.get()) or (not apellidoP.get()) or (not apellidoM.get()):
            mensaje = messagebox.showerror('¡Error!','Favor de llenar los campos')
        else:
            try:
                comandos = db.cursor()
        
                mensaje = messagebox.askquestion('Modificar Empleado','¿Estás seguro de continuar con la operación?')
            
                if mensaje == 'yes':
                    query = 'UPDATE Empleados SET nombre = "{}", apellidoPaterno = "{}", apellidoMaterno = "{}", estado ="{}"  WHERE idEmpleado = {}'.format(nombre.get(), apellidoP.get(), apellidoM.get(), 1 if estado.get()=='Activo' else 0, idEmpleado.get())
                    comandos.execute(query)
                    db.commit()
                    self.borrarAlterno(idEmpleado,nombre,apellidoP,apellidoM)
                    estado.current(0)
            except Exception as e:
                mensaje = messagebox.showerror('¡Error!','No se pudo acceder a la base de datos.')