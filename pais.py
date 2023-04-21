from variables import TABLA_PAISES, LISTA_PAISES

def cargarPaises():
    archivo = open(TABLA_PAISES)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))

    for pais in salida:
        if pais not in LISTA_PAISES:
            LISTA_PAISES.append(pais)

def getPais(cod):
    for pais in LISTA_PAISES:
        if pais[0] == cod:
            return pais
    print("No se encontro el pais")
    return False

def addPais():
    codPais = str(int(input("Ingrese el codigo del pais: ")))
    if paisExist(codPais): # validar que el pais no este repetido
        print("Este pais ya existe")
        return "Codigo repetido"
    nombrePais = input("Ingrese el nombre del pais: ")
    
    nuevo = [codPais, nombrePais]
    LISTA_PAISES.append(nuevo)
    print("Nuevo pais agregado")

# funcion que retorna si un codigo de pais esta en la lista o no
def paisExist(cod):
    for pais in LISTA_PAISES:
        if pais[0] == cod:
            return True
    return False

def deletePais(pais):
    if pais == False:
        print("No existe este pais")
        return False
    with open(TABLA_PAISES, "r") as f:
        lines = f.readlines()
    with open(TABLA_PAISES, "w") as f:
        for line in lines:
            if line.strip("\n").split(";") != pais:
                f.write(line)
        print("Pais eliminado")


def modificarPais(pais):
    if pais == False:
        return False
    
    opcion = input("Que desea modificar?\n[1]ID\n[2]Nombre\n> ")
    if opcion == "1":
        idPais = str(int(input("Ingrese el nuevo id: ")))
        while paisExist(idPais) == True:
            print("Este id ya existe, intente con otro")
            idPais = str(int(input("Ingrese el nuevo id: ")))
    if opcion == "2":
        nombre = input("Ingrese el nuevo nombre: ")
    
    with open(TABLA_PAISES, "r") as f:
        lines = f.readlines()
    with open(TABLA_PAISES, "w") as f:
        for line in lines:
            if line.strip("\n").split(';') != pais:
                f.write(line)
            if line.strip("\n").split(';') == pais:
                if opcion == "1":
                    f.write(f"{idPais};{pais[1]}\n")
                if opcion == "2":
                    f.write(f"{pais[0]};{nombre}\n")
        print("Pais modificado")