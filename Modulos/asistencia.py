#Definir clase asistencia
class Asistencia:
    def __init__(self, id_asistencia, fecha_asistencia, estado_asistencia, 
                 id_alumno, id_materia):
        
        self.id_asistencia = id_asistencia
        self.fecha_asistencia = fecha_asistencia
        self.estado_asistencia = estado_asistencia
        self.id_alumno = id_alumno
        self.id_materia = id_materia
