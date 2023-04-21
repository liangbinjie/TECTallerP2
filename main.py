from os import system
from insercion import menuInsercion
from busqueda import menuBusqueda
from pais import cargarPaises
from ciudad import cargarCiudad
from cliente import cargarClientes
from mascota import cargarMascotas
# from modificar import menuModificar
# from eliminar import menuEliminar

cargarPaises()
cargarCiudad()
cargarClientes()
cargarMascotas()

def main():
    system('cls')
    running = True

    while running:
        system('cls')
        print("Que necesitas realizar?\n[1]Insercion\n[2]Busqueda\n[3]Eliminar\n[4]Modificar\n[5]Reportes\n")
        respuesta = input("> ")

        if respuesta == "1":
            system('cls')
            menuInsercion()

        elif respuesta == "2":
            system('cls')
            menuBusqueda()

        # elif respuesta == "3":
        #     system("cls")
        #     menuEliminar()

        # elif respuesta == "4":
        #     system("cls")
        #     menuModificar()

        elif respuesta == "Q":
            running = False

        else:
            print("Opcion invalida")
            input()

if __name__ == '__main__':
    main()