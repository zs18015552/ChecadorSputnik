class Asistencia():
   
    def insertarAsistencia(self, idEmpleado, labelNombreEmpleado, db):
        comandos = db.cursor()
        query = 'SELECT CONCAT_WS(" ",e.nombre,e.apellidoPaterno,e.apellidoMaterno) AS nombreCompleto FROM Empleados AS e, Asistencia AS a WHERE e.idEmpleado=a.idEmpleado AND e.idEmpleado={} LIMIT 1'.format(idEmpleado)
        comandos.execute(query)
        resultados = comandos.fetchone()
        nombreEmpleado = resultados[0]

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

        