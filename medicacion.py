from variables import TABLA_MEDICACION,LISTA_MEDICACION,fechaV
from mascota import getMascota
from tratamiento import getTratamientos

def cargarMed():
    archivo = open(TABLA_MEDICACION)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))
    
    for medicamento in salida:
        if medicamento not in LISTA_MEDICACION:
            LISTA_MEDICACION.append(medicamento)

def Medexist(cod):
    for linea in LISTA_MEDICACION:
        if linea[0] == cod:
            return True
    else:
        return False

def getcodigoMed(cod):
    for linea in LISTA_MEDICACION:
        if linea[1] == cod:
            return True
    return False

def getMed():
    cod = input("Ingrese el ID de la medicacion: ")
    for medicacion in LISTA_MEDICACION:
        if  medicacion[1] == cod:
            return medicacion
    print("No se encontro el ID, intentelo de nuevo")
    return False       

def cargarMed():
    archivo = open(TABLA_MEDICACION)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))
    
    for medicamento in salida:
        if medicamento not in LISTA_MEDICACION:
            LISTA_MEDICACION.append(medicamento)


def getMedicacion(codMedicacion):
    for medicacion in LISTA_MEDICACION:
        if medicacion[1] == codMedicacion:
            return medicacion
    print("No se encontro la medicacion")
    return False

def getMedicacionMascota(idMascota):
    for medicacion in LISTA_MEDICACION:
        if medicacion[0] == idMascota:
            return medicacion
    print("No se encontro la medicicacion para la mascota")
    return False


def addMedicacion():
    idAnimal = str(int(input("Ingrese el id del animal: ")))
    mascota = getMascota(idAnimal)
    while mascota == False:
        idAnimal = str(int(input("Ingrese el id del animal: ")))
        mascota = getMascota(idAnimal)
    
    codMedicacion = str(int(input("Ingrese el codigo de medicacion: ")))
    while getcodigoMed(codMedicacion) == True:
        print("Este codigo ya existe, intente con otro")
        codMedicacion = str(int(input("Ingrese el codigo de medicacion: ")))
        getcodigoMed(codMedicacion)
    
    fecha = fechaV()
    tratamiento = getTratamientos()
    while tratamiento == False:
        tratamiento = getTratamientos()
    costoUnitario = int(input("Ingrese el costo unitario del tratamiento: "))
    cantidad = int(input("Ingrese la cantidad del tratamiento que desea recetar: "))
    total = costoUnitario * cantidad
    nuevo = [idAnimal, codMedicacion] + fecha + [tratamiento, costoUnitario, cantidad, total]
    LISTA_MEDICACION.append(nuevo)

    