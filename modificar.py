from pais import modificarPais, getPais
from os import system


def menuModificar():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de modificacion, que deseas modificar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n> ")
        if opcion == "1":
            idPais = input("Ingrese el id del pais: ")
            modificarPais(getPais(idPais))
        elif opcion == "2":
            pass
            # modificarCiudad()
        elif opcion == "3":
            pass
            # addCliente()
        elif opcion == "4":
            pass
            # addMascota()
        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls')   