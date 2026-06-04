#Definir clase asistencia
from conexion.conexion import Conexion

class Asistencia:
    def __init__(self, id_asistencia, fecha_asistencia, estado_asistencia, 
                 id_alumno, id_materia):
        
        self.id_asistencia = id_asistencia
        self.fecha_asistencia = fecha_asistencia
        self.estado_asistencia = estado_asistencia
        self.id_alumno = id_alumno
        self.id_materia = id_materia

    def guardar_Asistencia(self):
        conexion = Conexion.conectar()

        if conexion:

            cursor = conexion.cursor()
            #consulta sql para agregar alumnos
            sql = """
            INSERT INTO asistencia
            (Fecha, Estado, IdAlumno, IdMateria
            )
            VALUES (%s,%s,%s,%s) 
            """
            #valores para la tabla
            valores = (self.fecha_asistencia, self.estado_asistencia, self.id_alumno, self.id_materia
            )
            print("Guardando:", valores)
            cursor.execute(sql, valores)

            conexion.commit()

            cursor.close()
            conexion.close()

            return True

        return False