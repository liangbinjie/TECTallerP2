from variables import *
from pais import paisExist
from os import system
from visitas import repvisitas
from medicacion import repultmed
from tratamiento import reptrat
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


def getListaClientes():
    reporte = open("reportes/reporteClientes.txt", "a")
    for clientes in LISTA_CLIENTES:
        if clientes[0] != 1:
            reporte.write(f"ID: {clientes[0]} | Nombre: {clientes[1]} | Direccion: {clientes[2]} | Pais: {clientes[3]} | Ciudad: {clientes[4]} | Telefono: {clientes[5]} | Fecha: {clientes[6]}-{clientes[7]}-{clientes[8]} | Descuento: {clientes[9]} | Saldo: {clientes[10]}")

def menuReportes():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de reportes, que deseas reportar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n[5]Visitas\n[6]Tratamientos\n[7]Medicacion\n> ")
        if opcion == "1":
            getListaPaises()
        elif opcion == "2":
            getListaCiudadesPais()
        elif opcion == "3":
            getListaClientes()
            
        elif opcion == "4":
            pass
        elif opcion == "5":
           repvisitas()
        elif opcion == "6":
            reptrat()
        elif opcion == "7":
            repultmed()
        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls') 