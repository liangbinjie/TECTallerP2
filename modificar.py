from mascota import addMascota
from pais import modificarPais, getPais
from ciudad import modificarCiudad, getCiudad
from visitas import Modvisita
from os import system
from tratamiento import modTratamientos
from medicacion import modMedicamento
from cliente import modificarCliente, getCliente
from mascota import modificarMascota, getMascota

def menuModificar():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de modificacion, que deseas modificar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n[5]Visitas\n[6]Tratamientos\n[7]Medicacion\n[Q]Salir\n> ")
        if opcion == "1":
            idPais = input("Ingrese el id del pais: ")
            modificarPais(getPais(idPais))
        elif opcion == "2":
            idCiudad = input("Ingrese el id de la ciudad: ")
            modificarCiudad(getCiudad(idCiudad))
        elif opcion == "3":
            modificarCliente(getCliente(input("Ingrese el id del cliente: ")))
        elif opcion == "4":
            modificarMascota(getMascota(input("Ingrese el id de la mascota")))
        elif opcion == "5":
            Modvisita()
        elif opcion == "6":
            modTratamientos()
        elif opcion == "7":
            modMedicamento()
        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls')   