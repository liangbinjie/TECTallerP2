def getPaises():
    paises = open("database/paises.txt")
    listaPaises = []
    for linea in paises.readlines():
        listaPaises.append(linea.replace("\n", "").split(";"))
    return listaPaises


def getPais(cod):
    for pais in getPaises():
        if pais[0] == cod:
            return pais
    return False


def deletePais():
    pass

def addPais():
    print("Agregar pais")

def modificarPais():
    pass

def paisExist(cod):
    for pais in getPaises():
        if pais[0] == cod:
            return True
    return False