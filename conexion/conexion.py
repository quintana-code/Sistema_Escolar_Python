import mysql.connector

class Conexion:
    @staticmethod
    #Definiendo que esta clase no tiene algo que definir con el atributo 'self'
    def conectar():
        conexion= mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='bdasistencia', 
                                  port= '3306')
        return conexion
    