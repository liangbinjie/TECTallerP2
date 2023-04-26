from variables import *
from pais import paisExist

def getListaPaises():
    reporte = open("reportes/reportePais.txt", "a")
    for pais in LISTA_PAISES:
        print(pais)
        reporte.write(f"Codigo: {pais[0]} | Nombre: {pais[1]}\n")

def getListaCiudadesPais():
    codPais = input("Ingrese el codigo de pais: ")
    while paisExist(codPais) == False:
        print("Este pais no existe, ingrese otro")
        codPais = input("Ingrese el codigo de pais:")
    
    salida = f"** Codigo pais: {codPais} **"
    for ciudad in LISTA_CIUDADES:
        if ciudad[0] == codPais:
            print(f"\nCodigo ciudad: {ciudad[1]} | Nombre: {ciudad[2]}")
            salida += f"\nCodigo ciudad: {ciudad[1]} | Nombre: {ciudad[2]}"
    
    reporte = open("reportes/reporteCiudades.txt", "a")
    reporte.write(salida)


def menuReportes():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de eliminar, que deseas eliminar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n[5]Medicacion\n> ")
        if opcion == "1":
            getListaPaises()
        elif opcion == "2":
            getListaCiudadesPais()
        elif opcion == "3":
            pass
            
        elif opcion == "4":
            pass
        elif opcion == "5":
           pass
        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls') 