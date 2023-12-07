class Recurso:
    def __init__(self,codigo,nombre,estado):
        self.codigo=codigo
        self.nombre=nombre
        self.estado=estado
    def __str__(self):
        return(f'nombre: {self.nombre},codigo: {self.codigo}, estado: {self.estado}')
        
        