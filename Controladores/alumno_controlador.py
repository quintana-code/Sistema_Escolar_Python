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
    
#--------------------------------------------alumnos pero para el admin----------------------------------------------------------------------
    @staticmethod
    def obtener_alumnos_admin():

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """SELECT IdAlumno, Nombre, Grupo FROM alumno"""
        cursor.execute(sql)
        alumnos = cursor.fetchall()

        cursor.close()
        conexion.close()
        return alumnos
#-----------------------------------eliminar----------------------------------------------------------
    @staticmethod
    def eliminar_alumno(id_alumno):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = "DELETE FROM alumno WHERE IdAlumno = %s"

        try:
            cursor.execute(sql, (id_alumno,))
            conexion.commit()
            return True

        except Exception as e:
            print("Error al eliminar alumno: ", e)
            return False
        #para terminar....
        finally:
            cursor.close()
            conexion.close()

    #-----------------------------------editar----------------------------------------------------------
    @staticmethod
    def editar_alumno(id_alumno, nombre, grupo):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """UPDATE alumno SET Nombre = %s, Grupo = %s WHERE IdAlumno = %s"""

        try:
            cursor.execute(sql, (nombre, grupo, id_alumno))
            conexion.commit()
            return True

        except Exception as e:
            print("Error al editar alumno: ", e)
            return False

        finally:
            cursor.close()
            conexion.close()
    #-----------------------------------agregar----------------------------------------------------------
    @staticmethod
    def agregar_alumno(id_alumno, nombre, grupo):

        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """INSERT INTO alumno (IdAlumno, Nombre, Grupo) VALUES (%s, %s, %s)"""

        try:
            cursor.execute(sql, (id_alumno, nombre, grupo))
            conexion.commit()
            return True

        except Exception as e:
            print("Error al agregar alumno: ", e)
            return False

        finally:
            cursor.close()
            conexion.close()
