from json import *


base_registro_admins = []
base_registro_estudiantes = []
#VALIDACION DE ARCHIVO REGISTROS EN CARPETA BD
try:
    with open(f"bd/Registros.json") as archivo:
        base_registro_admins = load(archivo)
except:
    print("No hay productos guardados...")
    

#VALIDACION DE ARCHIVO REGISTROS_ESTUDIANTES EN CARPETA BD
try:
    with open(f"bd/Registros_estudiantes.json") as archivo:
        base_registro_estudiantes = load(archivo)
except:
    print("No hay productos guardados...")



def registro_profes_admins():
    
    registro_ad_pro = {
        "id" : input("Ingrese su id: "),
        "nombre" : input("Ingrese su nombre: "),
        "cargo" : input("Ingrese su cargo: "),
        "email" : input("Ingrese su email: "),
        "clave" : input("Ingrese su contraseña: ")
    }
    base_registro_admins.append(registro_ad_pro)
    
    with open(f"bd/Registros.json", "w") as archivo:
        data_cuenta = dumps(base_registro_admins)
        archivo.write(data_cuenta)
        
        
        
        
        
        
def registro_estudiantes():
    registro_estudiante = {
        "id" : input("Ingrese su id: "),
        "nombre" : input("Ingrese su nombre: "),
        "apellido" : input("Ingrese su apellido: "),
        "email" : input("Ingrese su email: "),
        "fecha nacimiento" : input("Ingrese su fecha de nacimiento: ")
    }
    base_registro_estudiantes.append(registro_estudiante)
    
    with open(f"bd/Registros_estudiantes.json", "w") as archivo:
        data_cuenta = dumps(base_registro_estudiantes)
        archivo.write(data_cuenta)
        
