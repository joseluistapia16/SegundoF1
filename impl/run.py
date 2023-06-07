from procesos.menus import *
from dominio.entidades import *
from data.data import *
from archivos.archivos import *
class Run:

    def __init__(self):
        self.ruta="C:/Users/Usuario/PycharmProjects/SegundoF1/segundoF.csv"
        self.arch = ArchivoF()
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
        if op == 3:
            self.__actualizar()
            self.start()
        if op== 4:
            self.__eliminar()
            self.start()
        if op==5:
            self.__listar()
            self.start()


    def __registro(self):
        print("\t\tREGISTRO DE CLIENTES")
        cedula = input("Cedula:")
        self.lista= self.arch.getClients(self.ruta)
        pos = self.dat.getClientId(cedula,self.lista)
        if pos==-1:
            nombre = input("Nombre:")
            telefono = input("Telefono:")
            codigo = input("Codigo:")
            obj = Cliente(cedula,nombre,telefono,codigo)
            datos = obj.getCedula()+";"+obj.nombre+";"+obj.telefono+";"+obj.codigo+";\n"
            self.arch.create(self.ruta,datos,"a")
            print("Datos guardados!")
        else:
            print("Cedula ya existe!")
        input("<Enter> para continuar...")

    def __listar(self):
        print("\t\tLISTADO DE CLIENTES")
        self.lista= self.arch.getClients(self.ruta)
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

    def __actualizar(self):
        print("\t\tACTUALIZACION DE DATOS DE CLIENTES")
        cedula = input("Cedula:")
        pos = self.dat.getClientId(cedula,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            nombre = input("Nombre:")
            telefono = input("Telefono:")
            codigo = input("Codigo:")
            self.lista[pos].nombre = nombre
            self.lista[pos].telefono = telefono
            self.lista[pos].codigo = codigo
            print("Datos actualizados!")
        else:
            print("Cedula no exsiste!")
        input("<Enter> para continuar...")

    def __eliminar(self):
        print("\t\tELIMINACION DE DATOS DE CLIENTES")
        cedula = input("Cedula:")
        pos = self.dat.getClientId(cedula,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            self.lista.pop(pos)
            print("Datos eliminados!")
        else:
            print("Cedula no existe!")
        input("<Enter> para continuar...")




