from os import system
from pais import addPais
from ciudad import addCiudad
from cliente import addCliente
from mascota import addMascota


def menuInsercion():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de insercion, que deseas agregar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n> ")
        if opcion == "1":
            addPais()
        elif opcion == "2":
            addCiudad()
        elif opcion == "3":
            addCliente()
        elif opcion == "4":
            addMascota()
        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls')   
        