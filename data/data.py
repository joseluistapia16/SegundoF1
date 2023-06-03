from dominio.entidades import *
class Data:

    def getClient(self,cedula,lista):
        obj = None
        for i in range(len(lista)):
            if cedula == lista[i].getCedula():
                obj = lista[i]
                break
        return obj
