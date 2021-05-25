from tkinter import *
from datetime import date
from tkinter import messagebox

class DiaFestivo():

    def registrarDiaFestivo(self, calendario, db):
        if not (calendario.selection_get()):
            messagebox.showerror('¡Error!','Favor de seleccionar una fecha.')
        
        else:
            mensaje = messagebox.askquestion('Registar Dia Festivo','¿Estás seguro que la información es correcta?')

            if mensaje=='yes':
                try:
                    comandos = db.cursor()
                    query = 'SELECT fecha FROM DiaFestivo WHERE fecha="{}" AND estado=1'.format(calendario.selection_get())
                    comandos.execute(query)
                    repetido = comandos.fetchone()

                    if not repetido:
                        query = 'INSERT INTO DiaFestivo (fecha) VALUES ("{}");'.format(calendario.selection_get())
                        comandos.execute(query)
                        messagebox.showinfo('Registro Día Festivo','Día registrado con éxito.')
                        calendario.selection_set(date.today())
                    
                    else:
                        messagebox.showerror('Registro Día Festivo','Día repetido.')

                except Exception as e:
                    messagebox.showerror('Registro Día Festivo','No se pudo registrar el día festivo. ' + str(e))

    def listarDiasFestivos(self, db):
        try:
            comandos = db.cursor()
            comandos.execute('SET lc_time_names = "es_MX"')
            comandos.execute('SELECT idFestivo, dayname(fecha), day(fecha), monthname(fecha), year(fecha) FROM DiaFestivo WHERE estado=1 ORDER BY IdFestivo')
            dias = comandos.fetchall()

            return dias

        except Exception as e:
            messagebox.showerror('Día Excepcion','No se pudieron listar los días festivos. ' + str(e))

    def eliminarDiaFestivo(self,tabla,db):
        if not (tabla.selection()):
            messagebox.showerror('¡Error!','Favor de seleccionar un día a eliminar.')
        
        else:
            mensaje = messagebox.askquestion('Eliminar Dia Festivo','¿Estás seguro deseas proceder con la operación?')

            if mensaje=='yes':
                for cosa in tabla.selection():
                    idDia = tabla.item(cosa,"text")

                try:
                    comandos = db.cursor()

                    query = "UPDATE DiaFestivo SET estado = 0 WHERE idFestivo ={}".format(str(idDia))
                    comandos.execute(query)
                    db.commit()

                    mensaje = messagebox.showinfo('Eliminar Día Festivo','Día eliminado con éxito.')

                    comandos.execute('SET lc_time_names = "es_MX"')
                    comandos.execute('SELECT idFestivo, dayname(fecha), day(fecha), monthname(fecha), year(fecha) FROM DiaFestivo WHERE estado=1 ORDER BY IdFestivo')
                    dias = comandos.fetchall()

                    tabla.delete(*tabla.get_children())

                    for dia in dias:
                        tabla.insert('', END, text=dia[0], values=(dia[0],"{} {} de {} de {}".format(dia[1], str(dia[2]), dia[3], str(dia[4]))))

                except Exception as e:
                    messagebox.showerror('Eliminar Día Festivo','No se pudo eliminar el día festivo. '+ str(e))

      