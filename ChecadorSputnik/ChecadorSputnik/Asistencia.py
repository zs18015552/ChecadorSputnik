from sshtunnel import SSHTunnelForwarder
import mysql.connector as mysql
from tkinter import *
from time import *
import threading

class Asistencia():

    def nombreEmpleado(idEmpleado):
        pass
    
    def insertarAsistencia(self, idEmpleado, labelNombreEmpleado):
        server = SSHTunnelForwarder(("198.54.125.222", 21098),
                                    ssh_host_key=None,
                                    ssh_username="axclzgpy",
                                    ssh_password="30dpr3538T@#alex",
                                    remote_bind_address=("127.0.0.1", 3306))

        server.start()

        try:
            db=mysql.connect(user='axclzgpy_sputnik',
                             password='jU0x3CV}Dv;c@wg67L',
                             host="127.0.0.1",
                             port=server.local_bind_port, 
                             database='axclzgpy_sputnik-VII')
            print("Conexión exitosa.")
        except Exception as e:
            print(e)
            print("Conexión fallida")
        
        print(idEmpleado)
        comandos = db.cursor()
        query = 'SELECT CONCAT_WS(" ",e.nombre,e.apellidoPaterno,e.apellidoMaterno) AS nombreCompleto FROM Empleados AS e, Asistencia AS a WHERE e.idEmpleado=a.idEmpleado AND e.idEmpleado={} LIMIT 1'.format(idEmpleado)
        comandos.execute(query)
        resultados = comandos.fetchone()
        print(resultados)
        nombreEmpleado = resultados[0]
        print (nombreEmpleado)

        labelNombreEmpleado.config(text=nombreEmpleado, fg='black')

        comandos.execute('SELECT idEmpleado from Asistencia WHERE DATE(fechaHora) = CURDATE()')
        resultados = comandos.fetchall()
        contador = 0

        for resultado in resultados:
            contador = contador + 1

        if (contador%2==0):
            query='INSERT INTO Asistencia (chequeo,idEmpleado) VALUES ("SALIDA","{}")'.format(idEmpleado)
        else:
            query='INSERT INTO Asistencia (chequeo,idEmpleado) VALUES ("ENTRADA","{}")'.format(idEmpleado)
        
        comandos.execute(query)

        db.close()
        server.stop()
        