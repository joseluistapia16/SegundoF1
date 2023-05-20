def getMenu(tupla):
    for i in range(len(tupla)):
        pr = str(i+1)+".- "+tupla[i]+"."
        print(pr)
    op = 0
    while op<1 or op> len(tupla):
        pi ="Ingrese una opcion[1.."+str(len(tupla))+"]:"
        op = int(input(pi))
    return op