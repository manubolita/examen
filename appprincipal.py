from recurso import *
from usuario import *
from prestamo import *
from central_prestamos import *
import os
def MenuManejoRecursos(central):
    while True:
        os.system("cls")
        print("-------------------------------------")
        print("1.adicionar recurso")
        print("2.consultar recurso")
        print("3.modificar recurso")
        print("4.mostrar recursos")
        print("5.eliminar recursos")
        print("6.salir")
        opcion=int(input("Opcion-> "))
        match opcion:
            case 1: 
                central.adicionar_recurso_interactivo()
                os.system("pause")
            case 2:
                central.consultar_recurso()
                os.system("pause")
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("regresando.....")
                break

            case other:
                print("El numero digitado no esta disponible")
                os.system("pause")
def MenuManejoUsuarios(central):
    while True:
        os.system("cls")
        print("-------------------------------------")
        print("1.Adicionar usuario")
        print("2.consultar usuario")
        print("3.modificar usuario")
        print("4.eliminar usuario")
        print("5.mostrar usuario")
        print("6.salir")
        opcion=int(input("Opcion-> "))
        match opcion:
            case 1: 
                central.agregar_usuario_interactivo()
                os.system("pause")
            case 2:
                central.consultar_Usuario()
                os.system("pause")
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                print("regresando.....")
                break

            case other:
                print("El numero digitado no esta disponible")
                os.system("pause")
def MenuManejoPrestamos(central):
    while True:
        os.system("cls")
        print("-------------------------------------")
        print("1.prestamo de recurso")
        print("2.devolucion de un recurso")
        print("3.mostrar prestamo usuario")
        print("4.mostrar prestamos Usuarios")
        print("5.salir")
        opcion=int(input("Opcion-> "))
        match opcion:
            case 1: 
                central.prestamo_recursos()
                os.system("pause")
            case 2:
                
                os.system("pause")
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("regresando.....")
                break

            case other:
                print("El numero digitado no esta disponible")
                os.system("pause")
def menuPrincipal():
    while True:
        os.system("cls")
        print("            Menu Principal            ")
        print("-------------------------------------")
        print("1.Manejo de Recursos")
        print("2.manejo Usuarios")
        print("3.manejo prestamos y devoluciones")
        print("4.salir")
        opcion=int(input("Opcion-> "))
        central=Central_Prestamo([],[],[])
        match opcion:
            case 1: 
                MenuManejoRecursos(central)
                os.system("pause")
            case 2:
                MenuManejoUsuarios(central)
                os.system("pause")
            case 3:
                MenuManejoPrestamos(central)
                os.system("pause")
            case 4:
                print("Fin del programa")
                break

            case other:
                print("El numero digitado no esta disponible")
                os.system("pause")
menuPrincipal()