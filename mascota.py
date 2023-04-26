from cliente import getCliente
from variables import TABLA_MASCOTAS, LISTA_MASCOTAS, fechaV

def cargarMascotas():
    listaMascotas = []
    archivo = open(TABLA_MASCOTAS)
    for linea in archivo.readlines():
        listaMascotas.append(linea.replace("\n", "").split(';'))

    for mascota in listaMascotas:
        if mascota not in LISTA_MASCOTAS:
            LISTA_MASCOTAS.append(mascota)


# Funcion para buscar una mascota por id
def getMascota(idMascota):
    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idMascota:
            return mascota
    print("No se encontro la mascota")
    return False
# getCliente("id", getMascotas())
def getMascotavisita(idMascota):
    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idMascota:
            return idMascota
    print("No se encontro la mascota")
    return False

def getMascotavisitamod(idMascota):
    cargarMascotas()
    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idMascota:
            return True
    print("No se encontro la mascota")
    return False

# Funcion para obtener las mascotas asociadas al cliente
def getMascotasCliente(idCliente):
    mascotasCliente = []
    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idCliente:
            mascotasCliente.append(mascota)

    return mascotasCliente

def deleteMascota():
    pass

def addMascota():
    # cliente exista
    # id mascota no repetido
    # NumCliente;IdAnimal;Nombre;tipomascota;raza;fechanacimiento;sexo;color; castrado; fechaultimavisita
    idCliente = getCliente(str(int(input("Ingrese el id del cliente: "))))
    while idCliente == False:
        idCliente = getCliente(str(int(input("Ingrese el id del cliente: "))))
    
    idAnimal = mascotaExist() # id no exista
    nombreAnimal = input("Ingrese el nombre del animal: ")
    tipoMascota = input("Ingres el tipo de mascota: ")
    raza = input("Ingrese la raza de la mascota: ")
    fechaN = fechaNacimiento()
    sexo = input("Ingrese el sexo de la mascota (hembra/macho): ")
    color = input("Ingrese el color de la mascota: ")
    castrado = input("Ingrese si esta castrado (si/no): ")
    fechaUltimaVisita = fechaV()
    # if fechaN[0] <= fechaUltimaVisita[0] and fechaN[1] <= fechaUltimaVisita[1]:
    nuevo = [idCliente[0], idAnimal, nombreAnimal, tipoMascota, raza] + fechaN + [sexo,color, castrado] + fechaUltimaVisita
    LISTA_MASCOTAS.append(nuevo)
    print("Mascota agregada")
    # else:
    #     print("Fecha ultima visita no es posterior a la fecha de nacimiento")


def modificarMascota():
    pass

def mascotaExist():
    encontrado = False

    idMascota = str(int(input("Ingrese el id de la mascota: ")))
    for mascota in LISTA_MASCOTAS:
        if mascota[1] == idMascota:
            encontrado = True
    
    if encontrado == True:
        print("ID de mascota ya existe, ingrese otro")
        return mascotaExist()

    else:
        return idMascota

def fechaNacimiento():
    ano = int(input("Ingrese el año de nacimiento de la mascota: "))
    mes = int(input("Ingrese el mes de nacimiento de la mascota: "))
    while mes > 12 or mes <= 0:
        print("Mes invalido, ingrese nuevamente")
        mes = int(input("Ingrese el mes de nacimiento de la mascota: "))
    dia = int(input("Ingrese el dia de nacimiento: "))
    if mes%2==1:
        while dia > 31 or dia <= 0:
            print("Dia invalido, ingrese nuevamente")
            dia = int(input("Ingrese el dia de nacimiento: "))
    else:
        while dia > 30 or dia <= 0:
            print("Dia invalido, ingrese nuevamente")
            dia = int(input("Ingrese el dia de nacimiento: "))
    return [dia,mes,ano]
