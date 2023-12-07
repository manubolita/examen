from recurso import *
from usuario import *
from prestamo import *
class Central_Prestamo:
    def __init__(self,recursos,usuarios,prestamos):
        self.recursos=recursos
        self.usuarios=usuarios
        self.prestamos=prestamos
    def adicionar_usuario(self,usuario):
        self.usuarios.append(usuario)
    def buscar_usuario(self,usuario):
        b=0
        for i in self.usuarios:
            if i.codigo==usuario.codigo:
                b=1
        if b==1:
            return True
        else:
            return False
    def agregar_usuario_interactivo(self):
        while True:
            nombre = input('Digite el nombre del Usuario ---> ')
            codigo = int(input('Digite el código del Usuario ---> '))
            tipo = input('Digite el tipo de usuario "1" para estudiante, "2" para docente y "3" para trabajador ---> ')

            usuario = Usuario(codigo, nombre, tipo)
            print(f'usuario--->{usuario}')
            if self.buscar_usuario(usuario):
                print('No se puede agregar el usuario, código en uso.')
            else:
                self.adicionar_usuario(usuario)
                print('usuario adicionado correctamente.')

            salir = input('Presione cualquier tecla para salir, o ingrese 1 para continuar: ')
            if salir != '1':
                break
    def consultar_Usuario(self):
        usuario=input('nombre del Usuario a buscar--->')
        b=0
        for i in self.usuarios:
            if i.nombre == usuario:
                b=1
                pos=i
        if b==1:
            return print(pos)
        else:
            return print('no se encontro el usuario')
        
    def adicionar_recurso(self, recurso):
        self.recursos.append(recurso)

    def buscar_recurso(self, recurso):
        b=0
        for i in self.recursos:
            if i.codigo == recurso.codigo:
                b=1
                
        if b==1:
            return True
        else:
            return False

    def adicionar_recurso_interactivo(self):
        while True:
            nombre = input('Digite el nombre del recurso ---> ')
            codigo = int(input('Digite el código del producto ---> '))
            estado = input('Digite el estado del producto "S" para disponible y "N" para no disponible ---> ')

            recurso = Recurso(codigo, nombre, estado)
            print(f'recurso--->{recurso}')
            if self.buscar_recurso(recurso):
                print('No se puede agregar el recurso, código en uso.')
            else:
                self.adicionar_recurso(recurso)
                print('Recurso adicionado correctamente.')

            salir = input('Presione cualquier tecla para salir, o ingrese 1 para continuar: ')
            if salir != '1':
                break
    def consultar_recurso(self):
        recurso=input('nombre del recurso a buscar--->')
        b=0
        for i in self.recursos:
            if i.nombre == recurso:
                b=1
                pos=i
        if b==1:
            return print(pos)
        else:
            return print('no se encontro el recurso')
    def mostrar_recursos(self):
        for i in self.recursos:
            print(i)
        
    def prestamo_recursos(self):
        usuario=input('digite el nombre de su usuario-->')
        y=True
        for i in self.usuarios:
            if i.nombre==usuario:
                y=False
                self.mostrar_recursos()
                recurso=input('digite el recurso a solicitar--->')
                for i in self.recursos:
                    if i.nombre == recurso:
                        pos=i
                if pos.estado==s:
                    print('el producto esta disponible')
                prestamo=Prestamo(pos,i)
                self.prestamos.append(prestamo)
                pos.estado=n
                break
        if y==True:
            print('usuario no valido,intentelo de nuevo o registrese correctamente')
    

                
    
            