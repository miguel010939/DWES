from operaciones import *
otra="s"
while otra=="s":
    x= int(input("Introduce un numero  "))
    y= int(input("Introduce otro numero  "))

    print("1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n")
    operacion=input("¿Que operacion desea hacer? (1-4)... ")
    resultado=0
    if operacion=="1":
        resultado=suma(x, y)
    elif operacion=="2":
        resultado=resta(x, y)
    elif operacion=="3":
        resultado=multiplicacion(x, y)
    elif operacion=="4":
        resultado=division(x, y)
    else:
        resultado="Operacion invalida! "

    print(resultado)
    otra=input("\n¿Quiere realizar otra operación? (s/n) ")
        




