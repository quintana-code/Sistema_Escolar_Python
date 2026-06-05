from conexion.conexion import Conexion

class Controlador_Reporte_Admin:
    @staticmethod
    def obtener_asistencias(fecha_inicio, fecha_fin):

        conexion = Conexion.conectar()

        if conexion:
            cursor = conexion.cursor()
            try:
                sql = """
                SELECT
                    a.IdAlumno,
                    a.Nombre,
                    asi.Fecha,
                    asi.Estado,
                    m.NombreMateria,
                    u.NombreUsuario
                FROM asistencia asi
                INNER JOIN alumno a
                    ON asi.IdAlumno = a.IdAlumno
                INNER JOIN materia m
                    ON asi.IdMateria = m.IdMateria
                INNER JOIN usuario u
                    ON m.IdUsuario = u.IdUsuario
                WHERE asi.Fecha BETWEEN %s AND %s
                ORDER BY asi.Fecha DESC
                """

                cursor.execute(sql,(fecha_inicio, fecha_fin))
                return cursor.fetchall()
            
            except Exception as e:
                print("Error al obtener asistencias:", e)
                return []

            finally:
                cursor.close()
                conexion.close()