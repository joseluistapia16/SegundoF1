class Metodos:

    def __init__(self,profesion):
        self._profesion=profesion

    def saludo(self,nombre):
        return "Hola "+nombre




class Banco:

    def __init__(self,nombre,n_agencias,telefono):
        self.nombre = nombre
        self.__n_agencias=n_agencias
        self.telefono = telefono

    def setN_agencias(self,n_agencias):
        self.__n_agencias=n_agencias

    def getN_Agencias(self):
        return self.__n_agencias

    def getData(self):
        return self.nombre+" "+str(self.__n_agencias)+" "+self.telefono

    def __prueba(self,nombre):
        print("Hola "+nombre)



class Persona:

    def __init__(self,cedula, nombre,telefono):
        self.__cedula= cedula
        self.nombre= nombre
        self.telefono = telefono

    def setCedula(self,cedula):
        self.__cedula= cedula

    def getCedula(self):
        return self.__cedula

    def getData(self):
        return self.__cedula+" "+self.nombre+" "+self.telefono

    def getFields(self):
        return "Cedula:"+self.__cedula+\
            "\nNombre:"+self.nombre+"\nTelefono:"+self.telefono


class Proveedor(Persona,Metodos):

    def __init__(self,cedula,nombre,telefono,codigo):
        Persona.__init__(self,cedula,nombre,telefono)
        self.codigo = codigo

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+self.telefono+" "+self.codigo

    def getFields(self):
        return "Cedula:" + self.getCedula() + \
            "\nNombre:" + self.nombre + "\nTelefono:" + self.telefono+ "\nCodigo:"+self.codigo

    def saludo(self,nombre):
        self._profesion="Programador"
        return "Hola "+self._profesion+" "+nombre

class Cliente(Persona):

    def __init__(self,cedula,nombre,telefono,codigo):
        Persona.__init__(self,cedula,nombre,telefono)
        self.codigo = codigo

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+self.telefono+" "+self.codigo

    def getFields(self):
        return "Cedula:"+self.getCedula()+\
            "\nNombre:"+self.nombre+"\nTelefono:"+self.telefono+"\nCodigo:"+self.codigo

class Factura:

    def __init__(self,n_factura,fecha,total):
        self.n_factura = n_factura
        self.fecha = fecha
        self.total = total

class Producto:

    def __init__(self,codigo,nombre,precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio





#Codigo de prueba
""" 
objB = Banco("CENTENARIO",56,"09876544")
print(objB.getData())
objB.nombre="PICHINCHA"
objB.setN_agencias(78)
print("N agencias:"+str(objB.getN_Agencias()))
print(objB.getData())

lista = []
objPr1 = Proveedor("09876","ANDREA VASQUEZ","0999876","PR001")
objPr2 = Proveedor("09545","MARIA FIGUEROA","067676","PR002")
objPr3 = Proveedor("35455","FRANKLIN VERA","098788","PR003")
objPr4 = Proveedor("54534","NATHALY PINCAY","097667","PR004")
lista.append(objPr1)
lista.append(objPr2)
lista.append(objPr3)
lista.append(objPr4)
for i in range(len(lista)):
    print(lista[i].getData())
"""
