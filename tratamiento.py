import code
from variables import LISTA_TRATAMIENTOS,TABLA_TRATAMIENTOS


def cargarTratamientos():
    archivo = open(TABLA_TRATAMIENTOS)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))

    for elemento in salida:
        if elemento not in LISTA_TRATAMIENTOS:
            LISTA_TRATAMIENTOS.append(elemento)

def getTratamientos():
    cod = input("Ingrese el ID del tratamiento: ")
    for tratamiento in LISTA_TRATAMIENTOS:
        if  tratamiento[0] == cod:
            return tratamiento
    print("No se encontro el tratamiento, intentelo de nuevo")
    return False


def getTratamientosFunc(cod):
    for tratamiento in LISTA_TRATAMIENTOS:
        if  tratamiento[0] == cod:
            return True
    return False

def Tratamientonum(cod):
    cargarTratamientos()
    i=0
    while i<len(LISTA_TRATAMIENTOS):
        if LISTA_TRATAMIENTOS[i][0]==cod:
            return i
        i=i+1
    return i


def getTratamientosNom(cod):
    for tratamiento in LISTA_TRATAMIENTOS:
        if  tratamiento[1] == cod:
            return True
    return False

def addTratamientos():
    idTrat = input("Ingrese el codigo del tratamiento nuevo: ")
    codigorep=getTratamientosFunc(idTrat)
    if codigorep==True:
        print("El codigo del tratamiento a ingresar ya esta utilizado")
        print("Por favor, ingrese la informacion nuevamente")
        addTratamientos()
    else:
        NomTrat= input("Ingrese el nombre del tratamiento nuevo:")
        NomTratrep=getTratamientosNom(NomTrat)
        if NomTratrep==True:
            print("El nombre que se quiere incluir ya esta en uso")
            print("Por favor, ingrese la informacion nuevamente")
            addTratamientos()
        else:
            precio = input("Ingrese el precio del objeto: ")
            nuevo = [idTrat,NomTrat,precio]
            LISTA_TRATAMIENTOS.append(nuevo)
def modTratamientos():
    cod = input("Ingrese el codigo del tratamiento cuyo precio sera cambiado:")
    if getTratamientosFunc(cod) == True:
        i=Tratamientonum(cod)
        precio = input("Ingrese el precio que desea interponer:")
        LISTA_TRATAMIENTOS[i]=LISTA_TRATAMIENTOS[i][:2]
        LISTA_TRATAMIENTOS[i]=LISTA_TRATAMIENTOS[i]+[precio]
        return LISTA_TRATAMIENTOS
    else:
        print("Codigo de tratamiento incorrecto, ingrese los datos de nuevo:")
        modTratamientos()



        
    
