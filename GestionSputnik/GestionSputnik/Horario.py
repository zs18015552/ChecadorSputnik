from tkinter import *
from tkinter import messagebox
from datetime import date

class Horario():

    def agregarTabla(self, comboDia, comboHoraInicio, comboHoraFin, tabla):
        if int(comboHoraInicio.get()[0:2])<int(comboHoraFin.get()[0:2]):
            bandera = True
            for linea in tabla.get_children():
                if (tabla.item(linea,"values") == ((comboDia.get(),comboHoraInicio.get(),comboHoraFin.get()))) or ((tabla.item(linea,"values")[0])==comboDia.get()):
                    message = messagebox.showerror('¡Error!','Horario repetido o inválido.')
                    bandera = False

            if bandera:
                tabla.insert('', END, text=comboDia.get(), values=(comboDia.get(),comboHoraInicio.get(),comboHoraFin.get()))

        else:
            messagebox.showerror('¡Error!','Horario inválido.')

    def eliminarTabla(self, tabla):
        if not (tabla.selection()):
            messagebox.showerror('¡Error!','Favor de seleccionar un día a eliminar.')

        else:
            tabla.delete(tabla.selection())

    def borrarTabla(self,tabla):
        tabla.delete(*tabla.get_children())

    def registrarHorario(self, comboEmpleado, comboDia, comboHoraInicio, comboHoraFin, tabla, db):
        if not (tabla.get_children()):
            messagebox.showerror('¡Error!','Tabla vacia.')
        else:
            mensaje = messagebox.askquestion('Registar Horario','¿Estás seguro que la información es correcta?')
            if mensaje=='yes':
                try:
                    id = comboEmpleado.get()[0:7]
                    valores=list()
                    for linea in tabla.get_children():
                        lista= (id,) + tabla.item(linea,"values")
                        valores.append(lista)

                    comandos = db.cursor()
                    query = 'UPDATE Horarios SET estado = 0 WHERE idEmpleado ={}'.format(id)
                    comandos.execute(query)
                    db.commit()
                    query='INSERT INTO Horarios (idEmpleado,dia,horaInicio,horaFin) VALUES (%s,%s,%s,%s)'
                    comandos.executemany(query,valores)
                    db.commit()
                    messagebox.showinfo('Registrar Horario','Registro de horario con éxito.')

                    tabla.delete(*tabla.get_children())
                    comboEmpleado.current(0)
                    comboDia.current(0)
                    comboHoraInicio.current(0)
                    comboHoraFin.current(0)

                except Exception as e:
                    messagebox.showerror('¡Error!','No se pudo registrar el horario. ' + str(e))

    def eliminarHorario(self,comboEmpleado, tabla,db):
        if not tabla.get_children():
            messagebox.showerror('¡Error!','La tabla de horarios está vacía. ')
        else:
            mensaje = messagebox.askquestion('Eliminar Horario','¿Estás seguro deseas proceder con la operación?')

            if mensaje=='yes':
                id = comboEmpleado.get()[0:7]        

                try:
                    comandos = db.cursor()

                    query = 'UPDATE Horarios SET estado = 0 WHERE idEmpleado ={}'.format(id)
                    comandos.execute(query)
                    db.commit()

                    messagebox.showinfo('Eliminar Horario','Horario eliminado con éxito.')

                    self.borrarTabla(tabla)

                except Exception as e:
                    messagebox.showerror('Eliminar Horario','No se pudo eliminar el horario. ' + str(e))

    def listarHorario(self, comboEmpleados, tabla, db):
        id = comboEmpleados.get()[0:7]

        try:
            comandos = db.cursor()
            comandos.execute('SET lc_time_names = "es_MX"')
            query='SELECT dia, horaInicio, horaFin FROM Horarios WHERE idEmpleado={} AND estado=1'.format(id)
            comandos.execute(query)
            dias = comandos.fetchall()

            tabla.delete(*tabla.get_children())

            for dia in dias:
                tabla.insert('', END, text=dia[0], values=(dia[0],str(dia[1]), str(dia[2])))

        except Exception as e:
            mensaje = messagebox.showerror('¡Error!','Error al acceder a la base de datos.')


