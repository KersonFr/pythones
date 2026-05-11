menu  = True
while menu:
    print("--menu--")
    print("1.- pago tarjeta de credito")
    print("2.- simulacion de compras")
    print("3.-salir")
    opc=int(input("Ingrese una opcion"))

    if opc==1:
        print("Pago tarjeta de credito")
    elif opc==2:
        print("Comprando")
    elif opc==3:
        print("chao")
        menu =False
    else:
        print("invalido")