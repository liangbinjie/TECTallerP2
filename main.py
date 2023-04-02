from os import system
from insercion import menuInsercion


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
            pass

        elif respuesta == "3":
            running = False

        else:
            print("Opcion invalida")
            input()

if __name__ == '__main__':
    main()