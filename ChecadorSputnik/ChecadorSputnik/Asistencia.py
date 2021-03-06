import time
import datetime
from tkinter import *
from tkinter import messagebox

class Asistencia():
    def insertarAsistencia(self, idEmpleado, labelNombreEmpleado, mensaje, db):
        comandos = db.cursor()
        
        #Consulta si el Id existe dentro de la base de datos de Empleado
        query = "SELECT idEmpleado from Empleados WHERE idEmpleado={}".format(idEmpleado.get())
        comandos.execute(query)
        empleado = comandos.fetchone()

        #Al no encontrar resultado de la consulta manda mensaje de error
        if not empleado:
            mensaje.config(text="Empleado no encontrado.")
            mensaje.update_idletasks()

        else:
            #Consulta el nombre y lo pone en el Label
            query = 'SELECT CONCAT_WS(" ",nombre,apellidoPaterno,apellidoMaterno) AS nombreCompleto FROM Empleados WHERE idEmpleado={} LIMIT 1'.format(idEmpleado.get())
            comandos.execute(query)
            resultados = comandos.fetchone()
            nombreEmpleado = resultados[0]
            labelNombreEmpleado.config(text=nombreEmpleado, fg='black')
            labelNombreEmpleado.update_idletasks()

            comandos.execute('SET lc_time_names = "es_MX"')
            query='SELECT DAYNAME(CURDATE()), TIME_TO_SEC(CURTIME())'
            comandos.execute(query)
            resultado = comandos.fetchone()
            diaCheck= resultado[0]
            horaCheck = int(resultado[1])

            query = 'SELECT dia, TIME_TO_SEC(horaInicio), TIME_TO_SEC(horaFin) FROM Horarios WHERE idEmpleado = {} AND dia = "{}" AND estado = 1'.format(idEmpleado.get(), diaCheck)
            comandos.execute(query)
            resultado = comandos.fetchone()
            
            if not resultado:
                mensaje.config(text="Imposible registrar, fuera de horario.")
                mensaje.update_idletasks()
            else:
                diaHorario = resultado[0]
                horaInicio = int(resultado[1])
                horaInicio15minMas = horaInicio + 900
                horaInicio15minMenos = horaInicio - 900
                horaFin = int(resultado[2])
                horaFin15minMas = horaFin + 900
                horaFin15minMenos = horaFin - 900

                query = 'SELECT idAsistencia, TIME_TO_SEC(horaEntrada), TIME_TO_SEC(horaSalida) FROM Asistencia WHERE fecha = CURDATE() AND idEmpleado = {}'.format(idEmpleado.get())
                comandos.execute(query)
                resultado = comandos.fetchone()

                if not resultado: 
                    query = 'INSERT INTO Asistencia (idEmpleado, horaEntrada) VALUES ("{}", DATE_SUB(NOW(), INTERVAL 1 HOUR))'.format(idEmpleado.get())
                    comandos.execute(query)
                    db.commit()

                    if (horaCheck >= horaInicio15minMenos) and (horaCheck <= horaInicio15minMas): 
                        mensaje.config(text="??Bienvenido!")
                        mensaje.update_idletasks()
                    else:
                        mensaje.config(text="??Bienvenido! Registro fuera de hora.")
                        mensaje.update_idletasks()

                else:
                    idAsistencia = resultado[0]
                    horaInicio = int(resultado[1])
                    horaFin = int(resultado[2])

                    if horaFin == 0:
                        query = 'UPDATE Asistencia SET horaSalida= DATE_SUB(NOW(), INTERVAL 1 HOUR) WHERE idAsistencia = {}'.format(idAsistencia)
                        comandos.execute(query)
                        db.commit()
                        if (horaCheck >= horaFin15minMenos) and (horaCheck <= horaFin15minMas): 
                            mensaje.config(text="??Hasta luego!")
                            mensaje.update_idletasks()
                        else:
                            mensaje.config(text="??Hasta luego! Registro fuera de hora.")
                            mensaje.update_idletasks()

                    else:
                        mensaje.config(text="Imposible registrar, ya existe registro del d??a.")
                        mensaje.update_idletasks()

        time.sleep(5)
        labelNombreEmpleado.config(text="<<Nombre>>", fg='gray')
        mensaje.config(text="")
        idEmpleado.delete(0,END)



        