from conexion.conexion import Conexion

class Controlador_Materia:
    @staticmethod

    def obtener_materia_por_usuario(id_usuario):
        conexion = Conexion.conectar()
        if conexion:

            cursor = conexion.cursor()
            sql = """SELECT IdMateria, NombreMateria FROM materia WHERE IdUsuario = %s"""
            cursor.execute(sql, (id_usuario,))
            materia = cursor.fetchone()

            cursor.close()
            conexion.close()

            return materia

        return None