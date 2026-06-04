from conexion.conexion import Conexion

class Controlador_Alumno:
    @staticmethod

    def obtener_alumnos():
        
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql1= """SELECT IdAlumno, Nombre FROM alumno """
        cursor.execute(sql1)
        alumnos = cursor.fetchall()
        #recupera todas las filas restantes del resultado de la consulta en la   base de datos
        conexion.close()
        cursor.close()
        return alumnos
