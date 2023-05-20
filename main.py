from procesos.operaciones import *
from procesos.menus import *
def funcion2():
    x1 = "POO"
    x2= "Hola"
    x3 = 30
    x4 = x1+x2+str(x3)+str(True)
    print(x4)

def funcion3():
    n1 = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))
    r = suma(n1,n2)
    print("Total:"+str(r))

def funcion4():
    edad = int(input("Edad:"))
    res = getAge(edad)
    print(res)
def funcion5():
    c= 0
    ci =0
    ac =0
    while c < 20:
        c = c+1
        if c%2!=0:
          print(c)
          ci = ci +1
          ac= ac +c
    print("La cantidad de impares es:"+str(ci))
    print("El total acumulado es:"+str(ac))

    ac = 0
    cp =0
    for i in range(1,11):
        if i % 2==0:
          cp = cp +1
          print(i)
          ac = ac +i

    print("Numero de pares es:"+str(cp))
    print("Valor acumulado de pares es:"+str(ac))

def funcion6():
    datos = ("2F",100,True,100.56,"POO")
    print(datos[2])
    datos = (True,100.56,"POO")
    #datos[3]=23
    for i in range(len(datos)):
        print(datos[i])
    lista = []
    lista.append(6)
    lista.append("2F")
    lista.append(100)
    lista.append(False)
    lista[2]=800
    #lista.pop(1)
    del lista[1]
    print(lista)
    for i in range(len(lista)):
        print(lista[i])
    lista.clear()
    print(len(lista))
    dic = {
        "2F" : 200,
        12  : "Jorge",
        False : (5,6,7,8),
        (5,8) : 123
    }
    dic[33]="POO"
    del  dic["2F"]
    dic[False]=1200
    print(dic[(5,8)])
    print(dic)

def funcion7():
    nombre = input("Nombre:")
    materia = input("Materia:")
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))
    n3 = float(input("Nota 3:"))
    r = getAverange(n1,n2,n3)
    msg = getMessage(r)
    if msg!="Valor incorrecto!":
        print("Promedio es:"+str(round(r,2)))
        print(msg)
    else:
        print(msg)

def funcion8():
    #hhh
    tupla = ("Registro","Consulta",
             "Actualizar","Eliminar",
             "Listar","Salir")
    op =getMenu(tupla)
    if op== 1:
        print("Python")
        input("<Enter> para continuar...")
        funcion8()

    if op==2:
        print("Java")
        input("<Enter> para continuar...")
        funcion8()
    if op==3:
        print("C++")
        input("<Enter> para continuar...")
        funcion8()




def funcion1():
    print("Hola Franklin")
    print("Segundo F")

#funcion8()
k = inputInt("Ingrese su edad:")
