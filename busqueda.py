from os import system
from pais import getPais
from ciudad import getCiudad
from cliente import getCliente
from mascota import getMascota

def menuBusqueda():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de busqueda, que deseas buscar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n> ")
        if opcion == "1":
            pais = getPais(input("Ingrese el codigo de pais: "))
            if pais != False:
                print(f"ID: {pais[0]}\n"+
                  f"Nombre: {pais[1]}")
        elif opcion == "2":
            ciudad = getCiudad(input("Ingrese el codigo de ciudad: "))
            if ciudad != False:
                print(f"ID Pais: {ciudad[0]}\n"+
                  f"ID Ciudad: {ciudad[1]}\n"+
                  f"Nombre: {ciudad[2]}")
        elif opcion == "3":
            cliente = getCliente(input("Ingrese el id del cliente: "))
            if cliente != False:
                print(f"ID: {cliente[0]}\n"+
                  f"Nombre: {cliente[1]}\n"+
                  f"Direccion: {cliente[2]}\n"+
                  f"Codigo pais: {cliente[3]}\n"+
                  f"Codigo ciudad: {cliente[4]}\n"+
                  f"Telefono: {cliente[5]}\n"+
                  f"Fecha ultima visita: {cliente[6]}-{cliente[7]}-{cliente[8]}\n"+
                  f"Porcentaje de despuesto: {cliente[9]}%\n"+
                  f"Saldo a deber: ${cliente[10]}")
        elif opcion == "4":
            mascota = getMascota(input("Ingrese el ID de la mascota: "))
            if mascota != False:
                print(f"ID cliente: {mascota[0]}\n"+
                      f"ID mascota: {mascota[1]}\n"+
                      f"Nombre mascota: {mascota[2]}\n"+
                      f"Tipo de mascota: {mascota[3]}\n"+
                      f"Raza mascota: {mascota[4]}\n"+
                      f"Fecha nacimiento de mascota: {mascota[5]}-{mascota[6]}-{mascota[7]}\n"+
                      f"Sexo de mascota: {mascota[8]}\n"+
                      f"Color de mascota: {mascota[9]}\n"+
                      f"Castrado: {mascota[10]}\n"+
                      f"Fecha ultima visita: {mascota[11]}-{mascota[12]}-{mascota[13]}\n")

        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls')   
