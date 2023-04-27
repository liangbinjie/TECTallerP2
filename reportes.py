from variables import *
from pais import paisExist
from os import system
from visitas import repvisitas
from medicacion import repultmed
from tratamiento import reptrat
from cliente import getCliente

def getListaPaises():
    reporte = open("reportes/reportePais.txt", "w")
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
    
    reporte = open("reportes/reporteCiudades.txt", "w")
    reporte.write(salida)


def getListaClientes():
    reporte = open("reportes/reporteClientes.txt", "w")
    for clientes in LISTA_CLIENTES:
        if clientes[0] != 1:
            reporte.write(f"ID: {clientes[0]} | Nombre: {clientes[1]} | Direccion: {clientes[2]} | Pais: {clientes[3]} | Ciudad: {clientes[4]} | Telefono: {clientes[5]} | Fecha: {clientes[6]}-{clientes[7]}-{clientes[8]} | Descuento: {clientes[9]} | Saldo: {clientes[10]}\n")

def getListaMascotasCliente():
    cliente = getCliente(input("Ingrese el id del cliente: "))
    if cliente != False:
        bandera = 0
        salida = f"** LISTA DE MASCOTAS PARA CLIENTE ID: {cliente[0]} **\n"
        for mascotas in LISTA_MASCOTAS:
            if mascotas[0] == cliente[0]:
                bandera = 1
                salida += f"ID: {mascotas[1]} | Nombre: {mascotas[2]} | Tipo: {mascotas[3]} | Raza: {mascotas[4]} | Fecha Nacimiento: {mascotas[5]}-{mascotas[6]}-{mascotas[7]} | Sexo: {mascotas[8]} | Color: {mascotas[9]} | Castrado: {mascotas[10]} | Fecha Ultima visita: {mascotas[11]}-{mascotas[12]}-{mascotas[13]}\n"
        
        if bandera == 0:
            print("Cliente no tiene mascotas")
        else:
            reporte = open("reportes/reporteMascotas.txt", "w")
            reporte.write(salida)
    else:
        print("No se encontro el cliente")


def clienteMasSaldo():
    mayor = 0
    for cliente in LISTA_CLIENTES:
        if int(cliente[10]) > mayor:
            mayor = int(cliente[10])
            infoCliente = cliente
    
    archivo = open("reportes/clienteMasSaldo.txt", "w")
    archivo.write(f"El cliente con mas saldo es {infoCliente[1]} con id: {infoCliente[0]}, con saldo de ${mayor}")
    print("reporte generado")

def clientesMasDescuento():
    mayor = 0
    for cliente in LISTA_CLIENTES:
        if int(cliente[9]) > mayor:
            mayor = int(cliente[9])
    
    archivo = open("reportes/clienteMasDescuento.txt", "w")
    for cliente in LISTA_CLIENTES:
        if int(cliente[9]) == mayor:
            archivo.write("Clientes con mayor descuento\n")
            archivo.write(f"Nombre: {cliente[1]} con id: {cliente[0]}, con descuento de {mayor}%\n")
    print("reporte generado")

def clientesCredito():
    listaMascotas = []
    for visita in LISTA_VISITAS:
        if visita[6] == "02":
            listaMascotas.append(visita[1])
    
    listaClientes = []
    for mascotas in listaMascotas:
        for mascota in LISTA_MASCOTAS:
            if mascotas == mascota[1]:
                if mascota[0] not in listaClientes:
                    listaClientes.append(mascota[0])
    
    reporte = open('reportes/reporteCredito.txt', "w")
    reporte.write("Lista de clientes de creditos\n")
    for cliente in listaClientes:
        reporte.write(f"ID: {cliente}\n")
    print(listaClientes)
    print("Reporte generado")


def tratamientoMasUtilizado():
    mayor = 0
    for medicacion in LISTA_MEDICACION:
        if int(medicacion[7]) > mayor:
            mayor = int(medicacion[7])
            medicina = medicacion[5]

    print(f"ID de tratamiento mas utilizado: {medicina}")
    reporte = open("reportes/tratamientoMasUtilizado.txt", "w")
    reporte.write("Tratamiento mas utilizado\n")
    reporte.write(f"ID de tratamiento mas utilizado: {medicina}")
    print("Reporte generado")
    

def menuReportes():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de reportes, que deseas reportar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n[5]Visitas\n[6]Tratamientos\n[7]Medicacion\n[8]Tratamiento mas utilizado\n> ")
        if opcion == "1":
            getListaPaises()
        elif opcion == "2":
            getListaCiudadesPais()
        elif opcion == "3":
            opcion2 = input("[1]Obtener lista de clientes\n[2]Clientes con mas saldo\n[3]Clientes de creditos\n[4]Clientes con mas descuentos\n> ")
            if opcion2 == "1":
                getListaClientes()
            elif opcion2 == "2":
                clienteMasSaldo()

            elif opcion == "3":
                clientesCredito()

            elif opcion == "4":
                clientesMasDescuento()
            
            
        elif opcion == "4":
            getListaMascotasCliente()
        elif opcion == "5":
           repvisitas()
        elif opcion == "6":
            reptrat()
        elif opcion == "7":
            repultmed()
        elif opcion == "8":
            tratamientoMasUtilizado()
        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls') 