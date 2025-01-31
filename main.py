from registro import *

opc = 0

while opc != 3:
    print("MENU\n1. RESGISTRO MAESTROS\n2. REGISTRO ESTUDIANTES")
    opc = int(input("Ingrese una opcion: "))
    match opc:
        case 1:
            print("REGISTRO ADMINISTRATIVOS\n")
            registro_profes_admins()
        case 2:
            print("REGISTRO ESTUDIANTES")
            registro_estudiantes()