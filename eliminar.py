from pais import deletePais, getPais
from os import system
from medicacion import eliminaMed

def menuEliminar():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de eliminar, que deseas eliminar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n[5]Medicacion\n> ")
        if opcion == "1":
            idPais = input("Ingrese el id del pais: ")
            deletePais(getPais(idPais))
        elif opcion == "2":
            pass
            # modificarCiudad()
        elif opcion == "3":
            pass
            # addCliente()
        elif opcion == "4":
            pass
            # addMascota()
        elif opcion == "5":
            eliminaMed()
        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls')   