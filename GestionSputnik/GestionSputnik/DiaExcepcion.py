from tkinter import *
from tkinter import messagebox
from datetime import date

class DiaExcepcion():

    def registrarDiaExcepcion(self, empleado, calendario, db):

        idEmpleado = empleado.get()[0:7]

        if not (calendario.selection_get()):
            mensaje = messagebox.showerror('¡Error!','Favor de seleccionar una fecha.')
        
        else:
            mensaje = messagebox.askquestion('Registar Día Excepción','¿Estás seguro que la información es correcta?')

            if mensaje=='yes':
                try:
                    comandos = db.cursor()

                    query = 'SELECT fecha FROM DiaExcepcion WHERE fecha="{}" AND idEmpleado="{}" AND estado=1'.format(calendario.selection_get(), idEmpleado)
                    comandos.execute(query)
                    repetido = comandos.fetchone()

                    if not repetido:
                        query = 'INSERT INTO DiaExcepcion (idEmpleado,fecha) VALUES ("{}","{}");'.format(idEmpleado, calendario.selection_get())
                        comandos.execute(query)
                        messagebox.showinfo('Registrar Día Excepcion','Día registrado con éxito.')

                        empleado.current(0)
                        calendario.selection_set(date.today())
                    else:
                        messagebox.showerror('Registro Día Excepción','Día repetido.')

                except Exception as e:
                    messagebox.showerror('Registrar Día Excepcion','No se pudo registrar el día de excepción del empleado.' + str(e))

    def listarDiasExcepcion(self, tabla, idEmpleado, db):

        id = idEmpleado.get()[0:7]

        try:
            comandos = db.cursor()
            comandos.execute('SET lc_time_names = "es_MX"')
            query='SELECT idExcepcion, dayname(fecha), day(fecha), monthname(fecha), year(fecha) FROM DiaExcepcion WHERE idEmpleado={} AND estado=1'.format(id)
            comandos.execute(query)
            dias = comandos.fetchall()

            tabla.delete(*tabla.get_children())

            for dia in dias:
                tabla.insert('', END, text=dia[0], values=(dia[0],"{} {} de {} de {}".format(dia[1], str(dia[2]), dia[3], str(dia[4]))))

        except Exception as e:
            messagebox.showerror('Día Excepción','No se pudo listar los días de excepción del empleado.' + str(e))

    def eliminarDiaExcepcion(self, combo, tabla, db):
        if not (tabla.selection()):
            messagebox.showerror('¡Error!','Favor de seleccionar un día a eliminar.')
        
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
                        tabla.insert('', END, text=dia[0], values=(dia[0],"{} {} de {} de {}".format(dia[1], str(dia[2]), dia[3], str(dia[4]))))

                except Exception as e:
                    mensaje = messagebox.showerror('Eliminar Día Excepción','No se pudo eliminar el día de excepción del empleado.' + str(e))