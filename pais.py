from variables import TABLA_PAISES, LISTA_PAISES, LISTA_CIUDADES

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
    
    for paises in LISTA_PAISES:
        if paises[0] == pais[0]:
            LISTA_PAISES.remove(paises)
    
    for ciudades in LISTA_CIUDADES:
        if ciudades[0] == pais[0]:
            LISTA_CIUDADES.remove(ciudades)

    print("Datos relacionados al pais eliminados")


def modificarPais(pais):
    if pais == False:
        return False
    
    nombre = input("Ingrese el nombre nuevo que deseas modificar para\n"+
                   f"{pais[0]}: {pais[1]}\n> ")
            
    for paises in LISTA_PAISES:
        if paises[0] == pais[0]:
            paises[1] = nombre
    
    print("Nombre de pais modificado")