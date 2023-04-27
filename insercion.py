from os import system
from pais import addPais
from ciudad import addCiudad
from cliente import addCliente
from mascota import addMascota
from visitas import addVisita
from tratamiento import addTratamientos
from medicacion import addMedicacion
def menuInsercion():
    running = True

    while running:
        opcion = input("Has ingresado al modulo de insercion, que deseas agregar\n[1]Pais\n[2]Ciudad\n[3]Cliente\n[4]Mascotas\n[5]Visitas\n[6]Tratamientos\n[7]Medicacion\n[Q]Salir\n>")
        if opcion == "1":
            addPais()
        elif opcion == "2":
            addCiudad()
        elif opcion == "3":
            addCliente()
        elif opcion == "4":
            addMascota()
        elif opcion == "5":
            addVisita()
        elif opcion == "6":
            addTratamientos()
        elif opcion == "7":
            addMedicacion()
        elif opcion == "Q":
            running = False
        else:
            print("Opcion invalida")
        input(">...Presione enter")
        system('cls')   
        