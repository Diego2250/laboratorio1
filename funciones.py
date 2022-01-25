def magnitud_signo(numero):
    signo=""
    resultado=""
    n1=numero[0]
    for i in range(len(numero)):
        resultado=resultado+str(numero[i])
    if n1==1:
        signo="-"
    else:
        signo="+"
    signo=signo+resultado
    return signo
def convertidor_cero_uno(numero):
    c1=[]
    resultado1=""
    resultado1int=0
    suma=0
    resultado2=""
    sumatoria = 0
    if numero[0]==1:
        for i in range(len(numero)):
            if numero[i]==1:
                c1.append(0)
            else:
                c1.append(1)

        for i in range(len(c1)):
            resultado1=resultado1+str(c1[i])
    else:
        for i in range(len(numero)):
            resultado1 = resultado1 + str(numero[i])
    ##return resultado
    if numero[0]==0:
        resultado2=resultado1
    else:
        resultado1int="0b"+str(resultado1)
        suma=(resultado1int+format(1, "b"))
        resultado2="0"+str(suma)
    return resultado2