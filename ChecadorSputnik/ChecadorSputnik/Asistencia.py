import time 
from tkinter import *
from tkinter import messagebox

class Asistencia():
    def borrar(self, nombre, idEmpleado):
        nombre.config(text="<<Nombre>>", fg='gray')
        idEmpleado.delete(0,END)

    def insertarAsistencia(self, idEmpleado, labelNombreEmpleado, db):
        comandos = db.cursor()
        
        #Consulta si el Id existe dentro de la base de datos de Empleado
        query = "SELECT idEmpleado from Empleados WHERE idEmpleado={}".format(idEmpleado.get())
        comandos.execute(query)
        resultado = comandos.fetchone()

        #Al no encontrar resultado de la consulta manda mensaje de error
        if not resultado:
            mensaje = messagebox.showerror('¡Error!','Empleado no existente.')
        else:
            #Consulta el nombre y lo pone en el Label
            query = 'SELECT CONCAT_WS(" ",nombre,apellidoPaterno,apellidoMaterno) AS nombreCompleto FROM Empleados WHERE idEmpleado={} LIMIT 1'.format(idEmpleado.get())
            comandos.execute(query)
            resultados = comandos.fetchone()
            nombreEmpleado = resultados[0]
            labelNombreEmpleado.config(text=nombreEmpleado, fg='black')
            labelNombreEmpleado.update_idletasks()

            #Consulta todas las asistencias del día y determina si el nuevo registro es Entrada o Salida
            query='SELECT idEmpleado from Asistencia WHERE DATE(fechaHora) = CURDATE() AND idEmpleado = {}'.format(idEmpleado.get())
            comandos.execute(query)
            resultados = comandos.fetchall()
            contador = 0

            for resultado in resultados:
                contador = contador + 1

            if (contador%2==0):
                query='INSERT INTO Asistencia (chequeo,idEmpleado) VALUES ("ENTRADA","{}")'.format(idEmpleado.get())
            else:
                query='INSERT INTO Asistencia (chequeo,idEmpleado) VALUES ("SALIDA","{}")'.format(idEmpleado.get())
        
            comandos.execute(query)

            time.sleep(5)
            labelNombreEmpleado.config(text="<<Nombre>>", fg='gray')
            idEmpleado.delete(0,END)



        