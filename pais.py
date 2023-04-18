from variables import TABLA_PAISES

def getPaises():
    paises = open(TABLA_PAISES)
    listaPaises = []
    for linea in paises.readlines():
        listaPaises.append(linea.replace("\n", "").split(";"))
    return listaPaises


def getPais(cod):
    for pais in getPaises():
        if pais[0] == cod:
            return pais
    print("No se encontro el pais")
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

def addPais():
    codPais = input("Ingrese el codigo del pais: ")
    if paisExist(codPais):
        print("Este pais ya existe")
        return "Codigo repetido"
    nombrePais = input("Ingrese el nombre del pais: ")
    # validar que el pais no este repetido
    
    with open(TABLA_PAISES, 'a') as f:
        nuevo = f'\n{codPais};{nombrePais}'
        f.write(nuevo)

def modificarPais(pais):
    if pais == False:
        return False
    
    opcion = input("Que desea modificar?\n[1]ID\n[2]Nombre\n> ")
    if opcion == "1":
        idPais = input("Ingrese el nuevo id: ")
        while paisExist(idPais) == True:
            print("Este id ya existe, intente con otro")
            idPais = input("Ingrese el nuevo id: ")
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

def paisExist(cod):
    for pais in getPaises():
        if pais[0] == cod:
            return True
    return False