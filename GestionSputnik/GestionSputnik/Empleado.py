from tkinter import *
from tkinter import messagebox

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
            messagebox.showerror('Día Excepcion','Error al obtener lista. ' + str(e))

    def consultarEmpleado(self, empleado, nombre, apellidoP, apellidoM, estado, db):        
        idEmpleado = empleado.get()[0:7]
        
        try:
            comandos = db.cursor()
            query = "SELECT nombre, apellidoPaterno, apellidoMaterno, estado FROM Empleados WHERE idEmpleado = {}".format(idEmpleado)
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

            else:
                mensaje = messagebox.showerror('¡Error!','Empleado no encontrado.')
        except Exception as e:
            mensaje = messagebox.showerror('¡Error!','No se pudo obtener el empleado. ' + str(e))

    def borrar(self, nombre, apellidoP, apellidoM):
        nombre.delete(0, END)
        apellidoP.delete(0, END)
        apellidoM.delete(0, END)
        nombre.focus()

    def altaEmpleado(self, idEmpleado, nombre,apellidoP, apellidoM, db):
        #Verifica que todos los campos este llenos
        if (not nombre.get()) or (not apellidoP.get()) or (not apellidoM.get()):
            messagebox.showerror('¡Error!','Favor de llenar todos los campos.')
        else:
            try:
                comandos = db.cursor()
        
                mensaje = messagebox.askquestion('Registar Empleado','¿Estás seguro que la información es correcta?')
            
                if mensaje == 'yes':
                    query = 'INSERT INTO Empleados (nombre,apellidoPaterno,apellidoMaterno) VALUES ("{}","{}","{}")'.format(nombre.get(),apellidoP.get(),apellidoM.get())
                    comandos.execute(query)
                    db.commit()
                    messagebox.showinfo("Alta Empleado","Empleado dado de alta con éxito.")
                    self.borrar(nombre,apellidoP,apellidoM)
                    idEmpleado.config(state='normal')
                    id = int(idEmpleado.get()) + 1
                    idEmpleado.delete(0,END)
                    idEmpleado.insert(0,id)
                    idEmpleado.config(state='disabled')
            except Exception as e:
                messagebox.showerror('¡Error!','No se pudo dar de alta al empleado. ' + str(e))

    def modificarEmpleado(self, empleado, nombre, apellidoP, apellidoM, estado, db):
        idEmpleado = empleado.get()[0:7]
        #Verifica que los campos esten llenos y modifica
        if (not nombre.get()) or (not apellidoP.get()) or (not apellidoM.get()):
            messagebox.showerror('¡Error!','Favor de llenar los campos')
        else:
            try:           
                mensaje = messagebox.askquestion('Modificar Empleado','¿Estás seguro de continuar con la operación?')
            
                if mensaje == 'yes':
                    comandos = db.cursor()
                    query = 'UPDATE Empleados SET nombre = "{}", apellidoPaterno = "{}", apellidoMaterno = "{}", estado ="{}"  WHERE idEmpleado = {}'.format(nombre.get(), apellidoP.get(), apellidoM.get(), 1 if estado.get()=='Activo' else 0, idEmpleado)
                    comandos.execute(query)
                    db.commit()
                    self.borrar(nombre,apellidoP,apellidoM)
                    estado.current(0)
                    valores = self.listar(db)
                    empleado.config(values=valores)
                    empleado.current(0)
            except Exception as e:
                messagebox.showerror('¡Error!','No se pudo modificar al empleado. ' + str(e))