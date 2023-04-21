from pais import paisExist
from variables import TABLA_CIUDADES, LISTA_CIUDADES

# Funcion para cargar el listado de las ciudades del txt
def cargarCiudad():
    archivo = open(TABLA_CIUDADES)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))

    for ciudad in salida:
        if ciudad not in LISTA_CIUDADES:
            LISTA_CIUDADES.append(ciudad)


# Funcion para obtener ciudad, pasando como parametro su codigo ciduad, retorna una lista
def getCiudad(codCiudad):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == codCiudad:
            return ciudad
    print("No se encontro la ciudad")
    return False
            
# Funcion para agregar una nueva ciudad
def addCiudad():
    codPais = str(int(input("Ingrese el codigo del pais: ")))
    while paisExist(codPais) == False: # mientras que el pais no exista
        print("Este pais no se encuentra en nuestra base de datos, ingrese otro")
        codPais = str(int(input("Ingrese el codigo del pais: ")))
    codCiudad = str(int(input("Ingrese el codigo de la ciudad: ")))
    while ciudadExist(codCiudad) == True: # mientras que la ciudad exista en la base de datos
        print("Esta ciudad ya existe en la base de datos, intente con otro")
        codCiudad = str(int(input("Ingrese el codigo de la ciudad: ")))
    nombre = input("Ingrese el nombre de la ciudad: ")

    nuevo = [codPais, codCiudad, nombre]
    LISTA_CIUDADES.append(nuevo)
    print("Nueva ciudad agregada")


# Funcion para verificar que ciudad exista
def ciudadExist(codCiudad):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == codCiudad:
            return True
    return False


# Funcion para obtener la info de una ciudad utilizando como parametro su codigo
def getCiudadInfo(codCiudad):
    for ciudad in LISTA_CIUDADES:
        if ciudad[1] == codCiudad:
            info = ciudad + LISTA_CIUDADES([int(ciudad[0])])
            print(info)
            return info
    else:
        print("No se pudo obtener informacion de esta ciudad")
        return False # No se encontro la ciudad

# Funcion para eliminar una ciudad
def deleteCiudad(ciudad):
    if ciudad == False:
        print("No existe esta ciudad")
        return False
        
    with open(TABLA_CIUDADES, "r") as f:
        lines = f.readlines()
    with open(TABLA_CIUDADES, "w") as f:
        for line in lines:
            if line.strip("\n").split(';') != ciudad:
                f.write(line)
    print("Ciudad eliminado")
#deleteCiudad(getCiudad("id"))
    

# Funcion para modificar una ciudad
def modificarCiudad(ciudad):
    if ciudad == False:
        return False
    
    opcion = input("Que desea modificar?\n[1]ID Pais\n[2]ID Ciudad\n[3]Nombre\n> ")
    if opcion == "1":
        idPais = str(int(input("Ingrese el nuevo id del pais: ")))
        while paisExist(idPais) == False:
            print("Este pais no existe, intente con otro")
            idPais = str(int(input("Ingrese el nuevo id del pais: ")))
    if opcion == "2":
        idCiudad = str(int(input("Ingrese el nuevo id de la ciudad: ")))
        while ciudadExist(idCiudad) == False:
            print("Esta ciudad no existe, intenta con otro")
            idCiudad = str(int(input("Ingrese el nuevo id de la ciudad: ")))
    if opcion == "3":
        nombre = input("Ingrese el nuevo nombre: ")
    
    else:
        return "Opcion invalido"
    
    with open(TABLA_CIUDADES, "r") as f:
        lines = f.readlines()
    with open(TABLA_CIUDADES, "w") as f:
        for line in lines:
            if line.strip("\n").split(';') != ciudad:
                f.write(line)
            if line.strip("\n").split(';') == ciudad:
                if opcion == "1":
                    f.write(f"{idPais};{ciudad[1]};{ciudad[2]}\n")
                if opcion == "2":
                    f.write(f"{ciudad[0]};{idCiudad};{ciudad[2]}\n")
                if opcion == "3":
                    f.write(f"{ciudad[0]};{ciudad[1]};{nombre}\n")
        print("Ciudad modificado")


