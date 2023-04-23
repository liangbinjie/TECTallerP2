
from variables import TABLA_VISITAS,LISTA_VISITAS,fechaV, LISTA_MASCOTAS, LISTA_CLIENTES
from mascota import getMascotavisita

def getVisitas():
    cod = input("Ingrese el ID de visita")
    for visita in LISTA_VISITAS:
        # print(visita)
        if  visita[0] == cod:
            return visita
    print("No se encontro la visita, intentelo de nuevo")
    return getVisitas()

def cargarVisitas():
    archivo = open(TABLA_VISITAS)
    salida = []
    for linea in archivo.readlines():
        salida.append(linea.replace("\n", "").split(";"))
    # print(salida)
    
    # for para verificar que no haya elementos repetidos
    for elemento in salida:
        if elemento not in LISTA_VISITAS:
            LISTA_VISITAS.append(elemento)

def addVisita():
    idVisita = visitexist()
    idAnimal = getMascotavisita(input('Ingrese el ID del animal: '))
    while idAnimal == False: # validar que el animal exista
        idAnimal = getMascotavisita(input('Ingrese el ID del animal: '))
    fecha= fechaV()    
    totalFactura = int(input("Ingrese el monto a pagar: "))
    formaPago = input("Ingrese la forma de pago 01 contado | 02 credito: ")
    descuento = 1
    if 1 <= totalFactura <= 99999:
        descuento = 0.97
    elif 100000 <= totalFactura < 101000:
        descuento = 0.95
    elif 150000 > totalFactura >= 101000:
        descuento = 0.9
    
    totalFactura = totalFactura * descuento
    
    if formaPago == "02":
        for mascota in LISTA_MASCOTAS:
            if mascota[1] == idAnimal:
                cliente = mascota[0]
        for clientes in LISTA_CLIENTES:
            if clientes[0] == cliente:
                clientes[10] = str(int(clientes[10]) + totalFactura)
                # clientes[9] = str((100-(descuento*100)))
    nuevo = [idVisita,idAnimal]+fecha+[totalFactura,formaPago]
    LISTA_VISITAS.append(nuevo)

def visitexist():
    cod = input("Ingrese el ID nuevo de visita: ")
    encontrado=False
    for visita in LISTA_VISITAS:
        if visita[0] == cod:
            encontrado=True
    if encontrado == True:
        print("ID de visita ya existe, ingrese otro")
        return visitexist()
    else:
        return cod 

num = 12
if 1 < num < 15:
    print('Num')
else:
    print("idk")