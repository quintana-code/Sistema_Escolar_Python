from conexion.conexion import Conexion

class Controlador_Reporte:
    @staticmethod

    def obtener_asistencias(fecha_inicio, fecha_fin, id_usuario):
        conexion = Conexion.conectar()

        if conexion:
            cursor = conexion.cursor()
            sql = """
            SELECT
                a.Nombre,
                asi.Fecha,
                asi.Estado,
                m.NombreMateria
            FROM asistencia asi
            INNER JOIN alumno a
                ON asi.IdAlumno = a.IdAlumno
            INNER JOIN materia m
                ON asi.IdMateria = m.IdMateria
            WHERE m.IdUsuario = %s
            AND asi.Fecha BETWEEN %s AND %s
            """

            cursor.execute(
                sql,
                (id_usuario, fecha_inicio, fecha_fin)
            )

            datos = cursor.fetchall()

            cursor.close()
            conexion.close()

            return datos

        return []