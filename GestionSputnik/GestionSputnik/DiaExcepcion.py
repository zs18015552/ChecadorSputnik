from tkinter import *
from tkinter import messagebox
from datetime import date

class DiaExcepcion():

    def registrarDiaExcepcion(self, empleado, calendario, db):

        idEmpleado = str(empleado.current() + 1000001)

        if not (calendario.selection_get()):
            mensaje = messagebox.showerror('¡Error!','Favor de seleccionar una fecha.')
        
        else:
            mensaje = messagebox.askquestion('Registar Día Excepción','¿Estás seguro que la información es correcta?')

            if mensaje=='yes':
                try:
                    comandos = db.cursor()

                    query = 'INSERT INTO DiaExcepcion (idEmpleado,fecha) VALUES ("{}","{}");'.format(idEmpleado, calendario.selection_get())
                    comandos.execute(query)
                    mensaje = messagebox.showinfo('Registrar Día Excepcion','Día registrado con éxito.')

                    empleado.current(0)
                    calendario.selection_set(date.today())
                except Exception as e:
                    mensaje = messagebox.showerror('Registrar Día Excepcion','Día registrado sin éxito.')

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

    def listarDiasExcepcion(self, tabla, idEmpleado, db):

        id = idEmpleado.get()[0:7]

        try:
            comandos = db.cursor()
            comandos.execute('SET lc_time_names = "es_MX"')
            query='SELECT idExcepcion, dayname(fecha), day(fecha), monthname(fecha), year(fecha) FROM DiaExcepcion WHERE idEmpleado={} AND estado=1'.format(id)
            comandos.execute(query)
            dias = comandos.fetchall()

            for dia in dias:
                tabla.insert('', "end", text=dia[0], values=(dia[0],"{} {} de {} de {}".format(dia[1], str(dia[2]), dia[3], str(dia[4]))))

        except Exception as e:
            print(e)
            mensaje = messagebox.showerror('Día Excepción','Error al acceder a la base de datos.')

    def eliminarDiaExcepcion(self, combo, tabla, db):
        if not (tabla.selection()):
            mensaje = messagebox.showerror('¡Error!','Favor de seleccionar un día a eliminar.')
        
        else:
            mensaje = messagebox.askquestion('Eliminar Dia Excepción','¿Estás seguro deseas proceder con la operación?')

            if mensaje=='yes':
                for cosa in tabla.selection():
                    idDia = tabla.item(cosa,"text")

                idEmpleado = combo.get()[0:7]

                try:
                    comandos = db.cursor()

                    query = "UPDATE DiaExcepcion SET estado = 0 WHERE idExcepcion ={}".format(str(idDia))
                    comandos.execute(query)
                    db.commit()

                    mensaje = messagebox.showinfo('Eliminar Día Excepción','Día eliminado con éxito.')

                    comandos.execute('SET lc_time_names = "es_MX"')
                    query='SELECT idExcepcion, dayname(fecha), day(fecha), monthname(fecha), year(fecha) FROM DiaExcepcion WHERE estado=1 AND idEmpleado={} ORDER BY IdExcepcion'.format(idEmpleado)
                    comandos.execute(query)
                    dias = comandos.fetchall()

                    tabla.delete(*tabla.get_children())

                    for dia in dias:
                        tabla.insert('', "end", text=dia[0], values=(dia[0],"{} {} de {} de {}".format(dia[1], str(dia[2]), dia[3], str(dia[4]))))

                except Exception as e:
                    print(e)
                    mensaje = messagebox.showerror('Eliminar Día Excepción','Día eliminado sin éxito.')