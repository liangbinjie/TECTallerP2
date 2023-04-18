from cliente import getCliente
from variables import TABLA_MASCOTAS

def getMascotas():
    listaMascotas = []
    archivo = open(TABLA_MASCOTAS)
    for linea in archivo.readlines():
        listaMascotas.append(linea.replace("\n", "").split(';'))

    # print(listaMascotas)
    return listaMascotas


# Funcion para buscar una mascota por id
def getMascota(idMascota):
    for mascota in getMascotas():
        if mascota[1] == idMascota:
            return mascota
    print("No se encontro la mascota")
    return False
# getCliente("id", getMascotas())


# Funcion para obtener las mascotas asociadas al cliente
def getMascotasCliente(idCliente):
    mascotasCliente = []
    for mascota in getMascotas():
        if mascota[1] == idCliente:
            mascotasCliente.append(mascota)

    return mascotasCliente

def deleteMascota():
    pass

def addMascota():
    # cliente exista
    # id mascota no repetido
    # NumCliente;IdAnimal;Nombre;tipomascota;raza;fechanacimiento;sexo;color; castrado; fechaultimavisita
    idCliente = getCliente(input("Ingrese el id del cliente: "))
    while idCliente == False:
        idCliente = getCliente(input("Ingrese el id del cliente: "))
    
    idAnimal = mascotaExist() # id no exista
    nombreAnimal = input("Ingrese el nombre del animal: ")
    tipoMascota = input("Ingres el tipo de mascota: ")
    raza = input("Ingrese la raza de la mascota: ")
    fechaN = fechaNacimiento()
    sexo = input("Ingrese el sexo de la mascota (hembra/macho): ")
    color = input("Ingrese el color de la mascota: ")
    castrado = input("Ingrese si esta castrado (si/no): ")
    fechaUltimaVisita = fechaV()
    with open(TABLA_MASCOTAS, 'a') as f:
        nuevo = f'\n{idCliente};{idAnimal};{nombreAnimal};{tipoMascota};{raza};{fechaN};{sexo};{color};{castrado};{fechaUltimaVisita}'
        f.write(nuevo)
    print("Mascota agregada")



def modificarMascota():
    pass

def mascotaExist():
    encontrado = False

    idMascota = input("Ingrese el id de la mascota: ")
    for mascota in getMascotas():
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
    return f'{dia};{mes};{ano}'

def fechaV():
    ano = int(input("Ingrese el ano de hoy: "))
    mes = int(input("Ingrese el mes de hoy: "))
    while mes > 12 or mes <= 0:
        print("Mes invalido, ingrese nuevamente")
        mes = int(input("Ingrese el mes de hoy: "))
    dia = int(input("Ingrese el dia de hoy: "))
    if mes%2==1:
        while dia > 31 or dia <= 0:
            print("Dia invalido, ingrese nuevamente")
            dia = int(input("Ingrese el dia de hoy: "))
    else:
        while dia > 30 or dia <= 0:
            print("Dia invalido, ingrese nuevamente")
            dia = int(input("Ingrese el dia de hoy: "))
    return f'{dia};{mes};{ano}'
# addMascota()