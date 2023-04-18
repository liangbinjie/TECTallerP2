from os import system
from insercion import menuInsercion
from busqueda import menuBusqueda
from modificar import menuModificar
from eliminar import menuEliminar

def main():
    system('cls')
    running = True

    while running:
        system('cls')
        print("Que necesitas realizar?\n[1]Insercion\n[2]Busqueda\n[3]Eliminar\n[4]Modificar\n[5]Reportes")
        respuesta = input("> ")

        if respuesta == "1":
            system('cls')
            menuInsercion()

        elif respuesta == "2":
            system('cls')
            menuBusqueda()

        elif respuesta == "3":
            system("cls")
            menuEliminar()

        elif respuesta == "4":
            system("cls")
            menuModificar()

        elif respuesta == "Q":
            running = False

        else:
            print("Opcion invalida")
            input()

if __name__ == '__main__':
    main()