def suma(a,b):
    r = (a+b)
    return r

def getAverange(z,x,y):
    return (z+x+y)/3

def getMessage(r):
    if r>10 or r<0:
        return "Valor incorrecto!"
    else:
        if r< 7 and r>=0:
            return "REPROBADO"
        if r>=7 and r<=10:
            return "APROBADO"
def getAge(edad):
    if edad>115 or edad<0:
        return "Edad invalida!!"
    else:
        if edad<= 10 and edad >=0:
            return "Infante"
        if edad>=11 and edad<=17:
            return "Adolecente!"
        if edad>=18 and edad<=25:
            return "Joven"
        if edad>=25 and edad<=64:
            return "Adulto!"
        if edad>=65 and edad<=115:
            return "Adulto Mayor!"

def inputInt(msg):
    x = -1
    while x < 0:
        try:
            x = int(input(msg))
        except:
            print("Valor invalido!")
            x = -1
    return x
