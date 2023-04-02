def getMascotas():
    listaMascotas = []
    archivo = open('database/mascotas.txt')
    for linea in archivo.readlines():
        listaMascotas.append(linea.replace("\n", "").split(';'))

    # print(listaMascotas)
    return listaMascotas


# Funcion para buscar una mascota por id
def getCliente(idMascota, listaMascostas):
    for mascota in listaMascostas:
        if mascota[0] == idMascota:
            return mascota
    print("No se encontro el cliente")
    return False
# getCliente("id", getMascotas())


# Funcion para obtener las mascotas asociadas al cliente
def getMascotasCliente(idCliente, listaMascotas):
    mascotasCliente = []
    for mascota in listaMascotas:
        if mascota[1] == idCliente:
            mascotasCliente.append(mascota)

    return mascotasCliente

def deleteMascota():
    pass

def addMascota():
    pass

def modificarMascota():
    pass

def mascotaExist():
    pass


