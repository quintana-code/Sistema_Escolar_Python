#conexion con BD
import mysql.connector

class Conexion:
    @staticmethod
    #Definiendo que esta clase no tiene algo que definir con el atributo 'self'
    def conectar():
        try:
            conexion= mysql.connector.connect(user='root', password='',
                                  host='localhost',
                                  database='bdasistencia', 
                                  port= '3306')
            print("Conexión exitosa")
            return conexion
        
        except mysql.connector.Error as e:
            print("Error en la conexión: ",e)
            return None 
        #retornar error cuando sql esta apagado o no hay conexion
    