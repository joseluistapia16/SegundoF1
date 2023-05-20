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


#Codigo de prueba
objB = Banco("CENTENARIO",56,"09876544")
print(objB.getData())