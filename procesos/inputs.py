class Inputs:

    def inputInt(self,msg):
        x = -1
        while x < 0:
            try:
                x = int(input(msg))
            except:
                print("Valor invalido!")
                x = -1
        return x