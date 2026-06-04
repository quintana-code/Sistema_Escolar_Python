#definir metodos para usuario
#importar la conecxión con la base de datos :3
from conexion.conexion import Conexion

class Controlador_Usuario:
    @staticmethod #para no definir self nuevamente
    def login(nombre_usuario, password):

        conexion = Conexion.conectar()
        if conexion == None:
            return None
        cursor = conexion.cursor()

        sql = """SELECT * FROM usuario WHERE NombreUsuario = %s AND Password =%s"""
        cursor.execute(sql, (nombre_usuario, password))
        usuario = cursor.fetchone() #Nos permitirà leer, procesar y descartar cada fila individualmente

        cursor.close()
        conexion.close()
        return usuario