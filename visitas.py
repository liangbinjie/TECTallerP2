
from variables import TABLA_VISITAS,LISTA_VISITAS,fechaV, LISTA_MASCOTAS, LISTA_CLIENTES
from mascota import getMascotavisita,getMascotavisitamod

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

def visitaexistsi(cod):
    encontrado=False
    for visita in LISTA_VISITAS:
        if visita[0] == cod:
            return True
    else:
        return False


def Modvisita():
    cod = input("Ingrese el ID de la visita:")
    if visitaexistsi(cod) == True:
        iddanim = input("Ingrese el ID de la mascota:")
        if getMascotavisitamod(iddanim) == True:
            codN = input("Ingrese la forma de pago que quiere modificar. Recuerde que las opciones son 01 contado | 02 credito:")
            if codN == '01' or codN == '02':
               numeronec=Buscainlista(cod)
               LISTA_VISITAS[numeronec]=LISTA_VISITAS[numeronec][:5]
               LISTA_VISITAS[numeronec]=LISTA_VISITAS[numeronec]+[codN]
               print( LISTA_VISITAS)
               return LISTA_VISITAS
            else:
                print("No ingreso ni 01 o 02, ingrese la informacion de nuevo:")
                Modvisita()
        else:
             print("Codigo de mascota no existe, ingrese la informacion de nuevo")
             Modvisita()
    else:
        print("Codigo de visita no existe, ingrese la informacion de nuevo")
        Modvisita()



def Buscainlista(codanim):
    f=0
    i=0
    cargarVisitas()
    while i<len(LISTA_VISITAS)-1:
        if LISTA_VISITAS[i][0]==codanim:
            return i
        i=i+1
    return i

def repvisitas():
    cod = input("Ingrese el codigo de la mascota para reportar sus visitas:")
    reportes = open ("reportes/reportesvisitas.txt","a")
    i=len(LISTA_VISITAS)-1
    bandera=0
    while i>=0:
        if LISTA_VISITAS[i][1]==cod:
            bandera=bandera+1
            reportes.write(f"Hubo una visita de la mascota codigo {cod} en: {LISTA_VISITAS[i]}\n")
        i=i-1
    if bandera==0:
        print("No se encontro el codigo de la mascota")
