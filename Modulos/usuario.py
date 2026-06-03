#Definir clase usuario
class Usuario: 
    def __init__(self, id_usuario, nombre_usuario, password, rol):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.rol = rol
        