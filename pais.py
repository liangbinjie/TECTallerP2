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


def deletePais():
    pass

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

def modificarPais():
    pass

def paisExist(cod):
    for pais in getPaises():
        if pais[0] == cod:
            return True
    return False