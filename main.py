from registro import *

opc = 0

while opc != 1:
    print("MENU\n1. RESGISTRO MAESTROS")
    opc = int(input("Ingrese una opcion: "))
    match opc:
        case 1:
            print("REGISTRO\n")
            registro_profes_admins()