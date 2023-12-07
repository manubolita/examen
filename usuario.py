class Usuario:
    def __init__(self,codigo,nombre,tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.tipo=tipo
    def __str__(self):
        return(f'nombre: {self.nombre},codigo: {self.codigo}, estado: {self.tipo}')
        