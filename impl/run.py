from procesos.menus import *
from dominio.entidades import *
from data.data import *
class Run:

    def __init__(self):
        self.men = MenuF()
        self.dat = Data()
        self.lista = []

    def start(self):
        tupla =("REGISTRO","CONSULTA","ACTUALIZAR",
                "ELIMINAR","LISTAR","SALIR")
        op = self.men.getMenu(tupla)
        if op==1:
            self.__registro()
            self.start()
        if op==2:
            self.__consulta()
            self.start()
        if op==5:
            self.__listar()
            self.start()


    def __registro(self):
        print("\t\tREGISTRO DE CLIENTES")
        cedula = input("Cedula:")
        nombre = input("Nombre:")
        telefono = input("Telefono:")
        codigo = input("Codigo:")
        obj = Cliente(cedula,nombre,telefono,codigo)
        self.lista.append(obj)
        print("Datos guardados!")
        input("<Enter> para continuar...")

    def __listar(self):
        print("\t\tLISTADO DE CLIENTES")
        for i in range(len(self.lista)):
            print(self.lista[i].getData())
        input("<Enter> para continuar...")

    def __consulta(self):
        print("\t\tCONSULTA DE CLIENTES")
        cedula = input("Cedula:")
        obj = self.dat.getClient(cedula,self.lista)
        if obj!= None:
            print(obj.getFields())
        else:
            print("Cedula no existe!!")
        input("<Enter> para continuar...")

