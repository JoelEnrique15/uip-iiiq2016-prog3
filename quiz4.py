try :
    continuar = 's'
    while continuar =='s':
        x= float(input("Introduce la temperatura:"))

        if x >= 37.5:
            archivo =open('temp.dat', 'a')
            archivo.write(str(x)+ " fiebre\n")
            print("tienes una temperatura de " + str(x) + "grados"+ "(tienes fiebre)")
            continuar =(input("para continuar presione s: "))
            if continuar != 's':
                print("adios")

        elif x<=30 and x>5:
            archivo = open('temp.dat', 'a')
            archivo.write(str(x) + " estas enfermo\n")
            print("tienes una temperatura de " + str(x) + "grados"+ "(estas enfermo)")
            continuar =(input("para continuar presione s: "))
            if continuar != 's':
                print("adios")

        elif x<= 5:
            archivo = open('temp.dat', 'a')
            archivo.write(str(x) + " tas frito x.x\n")
            print("tienes una temperatura de " + str(x) + "grados"+"(tas frito)")
            continuar =(input("para continuar presione s: "))
            if continuar != 's':
                print("adios")


except ValueError:
    print("valor invalido")

