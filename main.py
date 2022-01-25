##########Inicio del programa###########
from funciones import *
while True:
    #Se muestra el menú
    print("Elija una opción")
    print ("1. Ingresar numero binario")
    print ("2. Salir")
    opcion=input("-->")
    if opcion=="1":
        numero=[]
        print("Ingrese un numero binario de 8 bits")
        print("Ingrese primer dígito")
        numero.append(int(input()))
        print("Ingrese segundo dígito")
        numero.append(int(input()))
        print("Ingrese tercer dígito")
        numero.append(int(input()))
        print("Ingrese cuarto dígito")
        numero.append(int(input()))
        print("Ingrese quinto dígito")
        numero.append(int(input()))
        print("Ingrese sexto dígito")
        numero.append(int(input()))
        print("Ingrese septimo dígito")
        numero.append(int(input()))
        print("Ingrese octavo dígito")
        numero.append(int(input()))
        print("")
        print("Magnitud y signo:")
        print(magnitud_signo(numero))
        print("")
        print("Complemento a2:")
        print(convertidor_cero_uno(numero))
    elif opcion=="2":
        print("")
        print("Gracias, adios")
        break
