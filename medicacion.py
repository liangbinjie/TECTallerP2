
from variables import TABLA_MEDICACION,LISTA_MEDICACION,fechaV,REPORTESMEDICAMENTOS
from mascota import getMascotavisitamod,getMascota
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
        if linea[1] == cod:
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

def getMedicacionTrue(codMedicacion):
    for medicacion in LISTA_MEDICACION:
        if medicacion[1] == codMedicacion:
            return True
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

def medicamentoi(cod):
    i=0
    while i<len(LISTA_MEDICACION):
        if LISTA_MEDICACION[i][1]==cod:
            return i
        i=i+1
    return i 

def eliminaMed():
    codmed = input("Ingrese el codigo de la medicacion que desea borrar:")
    if Medexist(codmed)==True:
        i=medicamentoi(codmed)
        LISTA_MEDICACION.remove(LISTA_MEDICACION[i])

        print(LISTA_MEDICACION)
    else:
        print("Codigo de medicacion no existe, ingrese la informacion de nuevo")
        eliminaMed()


def modMedicamento():
    codmed = input("Ingrese el codigo de la medicacion:")
    if Medexist(codmed)==True:
        codanim = input("Ingrese el ID del animal:")
        if getMascotavisitamod(codanim) == True:
            nom = input("Ingrese el nuevo nombre del medicamento:")
            cant = input("Ingrese la cantidad nueva del medicamento:")
            precio = input("Ingrese el precio nuevo del medicamento:")
            precio=int(precio)
            cant=int(cant)
            preciototal=1
            preciototal=preciototal*precio*cant
            i=medicamentoi(codmed)
            LISTA_MEDICACION[i]=LISTA_MEDICACION[i][:5]
            LISTA_MEDICACION[i]=LISTA_MEDICACION[i]+[nom,precio,cant,preciototal]
            print(LISTA_MEDICACION)
        else:
            print("ID de animal no valido, ingrese la informacion de nuevo:")
            modMedicamento()
    else:
        print("Codigo de medicacion no valido, ingrese la informacion de nuevo:")
        modMedicamento()

def repultmed():
    cod = input("Ingrese el codigo de la mascota para reportar su ultima medicacion:")
    reportes = open ("reportes/reportesmedicamentos.txt","a")
    i=len(LISTA_MEDICACION)-1
    while i>=0:
        if LISTA_MEDICACION[i][0]==cod:
            reportes.write(f"Ultima medicacion de mascota codigo {cod}: {LISTA_MEDICACION[i][5]}\n")
            return 
        i=i-1
    print("No se encontro el codigo de la mascota")


    
