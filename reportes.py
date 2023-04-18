from variables import TABLA_PAISES
from pais import paisExist
from ciudad import getCiudades

def getListaPaises():
    with open(TABLA_PAISES) as f:
        for linea in f.readlines():
            print(linea)

def getListaCiudadesPais():
    codPais = input("Ingrese el codigo de pais: ")
    while paisExist(codPais) == False:
        print("Este pais no existe, ingrese otro")
        codPais = input("Ingrese el codigo de pais:")
    
    for ciudad in getCiudades():
        if ciudad[0] == codPais:
            print(ciudad)

getListaCiudadesPais()
    

