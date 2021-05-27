from tkinter import *
from tkinter import messagebox
from datetime import timedelta, date
from tkinter.filedialog import asksaveasfile
import csv
import os

class Reporte():

    def exportarCSV(self, empleado, fechaInicio, fechaFin, db):
        listaReporte = self.generarReporte(empleado, fechaInicio, fechaFin, db)

        listaCSV = [["Fecha","Hora Entrada","Hora Salida","Horas Efectivas"]]

        listaCSV = listaCSV + listaReporte

        archivo = asksaveasfile(mode='w',defaultextension='.csv')
        if not archivo:
            return
        writer = csv.writer(archivo,lineterminator='\r')
        writer.writerows(listaCSV)

        try: 
            os.startfile(archivo.name)
        except AttributeError:
            try: 
                subprocess.call(['open', archivo.name])
            except:
                messagebox.showerror('¡Error!','No se pudo abrir dirección URL')

        archivo.close()

    def listarFechas(self, fechaInicio, fechaFin):
        for fecha in range(int ((fechaFin - fechaInicio).days)+1):
            yield fechaInicio + timedelta(fecha)

    def generarReporte(self, empleado, fechaInicio, fechaFin, db):
        if not fechaInicio.get_date() > fechaFin.get_date():
            idEmpleado = empleado.get()[0:7]
            comandos = db.cursor()
            query = 'SELECT dia from Horarios WHERE idEmpleado = {} AND estado = 1'.format(idEmpleado)
            comandos.execute(query)
            resultados =comandos.fetchall()

            diasLaborales = list()
            listaDiasHorario = list()
            listaReporte = list()

            for resultado in resultados:
                if resultado[0] == 'lunes': diasLaborales.append(0)
                if resultado[0] == 'martes': diasLaborales.append(1)
                if resultado[0] == 'miércoles': diasLaborales.append(2)
                if resultado[0] == 'jueves': diasLaborales.append(3)
                if resultado[0] == 'viernes': diasLaborales.append(4)
                if resultado[0] == 'sábado': diasLaborales.append(5)
                if resultado[0] == 'domingo': diasLaborales.append(6)

            for fecha in self.listarFechas(fechaInicio.get_date(), fechaFin.get_date()):
                for dia in diasLaborales:
                    if fecha.weekday() == dia:
                        listaDiasHorario.append(fecha)
                        listaReporte.append([fecha.strftime("%Y-%m-%d"),"00:00:00","00:00:00",0])

            query = 'SELECT fecha, horaEntrada, TIME_TO_SEC(horaEntrada), horaSalida, TIME_TO_SEC(horaSalida) FROM Asistencia WHERE idEmpleado = {}'.format(idEmpleado)
            comandos.execute(query)
            listaAsistencias = comandos.fetchall()
            contadorLista = 0

            for dia in listaDiasHorario:
                for asistencia in listaAsistencias:
                    if dia==asistencia[0]:
                        listaReporte.pop(contadorLista)
                        listaReporte.insert(contadorLista,[dia.strftime("%Y-%m-%d"),str(asistencia[1]),str(asistencia[3]),int((asistencia[4] - asistencia[2] + 900)//3600)])
                contadorLista += 1

            query = 'SELECT fecha FROM DiaExcepcion WHERE idEmpleado = {} and estado = 1'.format(idEmpleado)
            comandos.execute(query)
            listaExcepciones = comandos.fetchall()

            contadorExcepcion = 0

            for dia in listaDiasHorario:
                for diaE in listaExcepciones:
                    if dia==diaE[0]:
                        listaReporte.pop(contadorExcepcion)
                        listaReporte.insert(contadorExcepcion,[dia.strftime("%Y-%m-%d"),"Excepción","",8])
                contadorExcepcion += 1

            query = 'SELECT fecha FROM DiaFestivo WHERE estado = 1'.format(idEmpleado)
            comandos.execute(query)
            listaFestivos = comandos.fetchall()

            contadorFestivos = 0

            for dia in listaDiasHorario:
                for diaF in listaFestivos:
                    if dia==diaF[0]:
                        listaReporte.pop(contadorFestivos)
                        listaReporte.insert(contadorFestivos,[dia.strftime("%Y-%m-%d"),"Festivo","",8])
                contadorFestivos += 1

            return listaReporte

        else:
            messagebox.showerror("¡Error!","Selección de fechas inválida.")

    def llenarTabla(self,tabla, empleado, fechaInicio, fechaFin, db):
            
        listaReporte = self.generarReporte(empleado, fechaInicio, fechaFin, db)
            
        tabla.delete(*tabla.get_children())

        for dia in listaReporte:
            tabla.insert('', END, text=dia[0], values=(dia[0],dia[1],dia[2],dia[3]))


