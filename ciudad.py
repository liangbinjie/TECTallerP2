from pais import getPaises, paisExist

# Funcion para obtener un listado de las ciudades
def getCiudades():
    ciudades = open("database/ciudades.txt")
    listaCiudades = []
    for linea in ciudades.readlines():
        listaCiudades.append(linea.replace("\n", "").split(";"))

    return listaCiudades


# Funcion para obtener ciudad, pasando como parametro su codigo ciduad, retorna una lista
def getCiudad(codCiudad):
    for ciudad in getCiudades():
        if ciudad[1] == codCiudad:
            return ciudad
    print("No se encontro la ciudad")
    return False


# Funcion para obtener la info de una ciudad utilizando como parametro su codigo
def getCiudadInfo(codCiudad):
    for ciudad in getCiudades():
        if ciudad[1] == codCiudad:
            info = ciudad + getPaises([int(ciudad[0])])
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
        
    with open("database/clientes.txt", "r") as f:
        lines = f.readlines()
    with open("prueba.txt", "w") as f:
        for line in lines:
            if line.strip("\n").split(';') != ciudad:
                f.write(line)
    print("Cliente eliminado")
#deleteCiudad(getCiudad("id"))
    


# Funcion para agregar una nueva ciudad
def addCiudad():
    codPais = input("Ingrese el codigo del pais: ")
    while paisExist(codPais) == False:
        print("Este pais no se encuentra en nuestra base de datos, ingrese otro")
        codPais = input("Ingrese el codigo del pais: ")
    codCiudad = input("Ingrese el codigo de la ciudad: ")
    nombre = input("Ingrese el nombre de la ciudad: ")

    with open('prueba.txt', 'a') as f:
        nuevo = f'\n{codPais};{codCiudad};{nombre}'
        f.write(nuevo)

    print("Nueva ciudad agregada")
# addCiudad()


# Funcion para modificar una ciudad
def modificarCiudad(ciudad):
    if ciudad == False:
        return False
    
    pass



# Funcion para verificar que ciudad exista
def ciudadExist():
    encontrado = False

    codCiudad = input("Ingrese el codigo de la ciudad: ")
    for ciudad in getCiudades():
        if ciudad[1] == codCiudad:
            encontrado = True
    