from ciudad import ciudadExist
from pais import paisExist
from variables import TABLA_CLIENTES

# Funcion para obtener la lista de clientes
def getClientes():
    listaClientes = []
    archivo = open(TABLA_CLIENTES)
    for linea in archivo.readlines():
        listaClientes.append(linea.replace("\n", "").split(';'))

    # print(listaClientes)
    return listaClientes
# getCliente()


# Funcion para buscar un cliente por id
def getCliente(idCliente):
    for cliente in getClientes():
        if cliente[0] == idCliente:
            # print(cliente)
            return cliente
    print("No se encontro el cliente")
    return False
# getCliente("id")


# Funcion para eliminar un cliente de la base de datos
def deleteCliente(cliente):
    if cliente == False:
        print("No existe este cliente")
        return False
    with open(TABLA_CLIENTES, "r") as f:
        lines = f.readlines()
    with open("prueba.txt", "w") as f:
        for line in lines:
            if line.strip("\n").split(';') != cliente:
                f.write(line)
    print("Cliente eliminado")
# deleteCliente(getCliente("id"))


# Funcion para agregar un cliente
def addCliente():
    # id autoincremental? || hacer funcion para actualizar los ids || o obtener ultimo id
    # cedula?
    idCliente = clienteExist() # verificar que no este repetido
    nombreCliente = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese el direccion del cliente: ")
    pais = input("Ingrese el codigo del pais: ")
    while paisExist(pais) == False:
        print("Este pais no existe en la base de datos, intente con otro")
        pais = input("Ingrese el codigo del pais: ")
    ciudad = input("Ingrese el codigo de la ciudad: ")
    while ciudadExist(ciudad) == False: # mientras que la ciudad no exista en la base de datos
        print("Esta ciudad no existe en la base de datos, intente con otro")
        ciudad = input("Ingrese el codigo de la ciudad: ")
    telefono = input("Ingrese el telefono del cliente: ")
    fecha = fechaV()
    descuento = int(input("Ingrese el porcentaje de descuento para el cliente: "))
    saldo = int(input("Ingrese el saldo a deber del cliente: "))
    with open('prueba.txt', 'a') as f:
        nuevo = f'\n{idCliente};{nombreCliente};{direccion};{ciudad};{telefono};{fecha};{descuento};{saldo}'
        f.write(nuevo)
# addCliente()


# Funcion para modificar el cliente
def modificarCliente(cliente):
    if cliente == False:
        return False
    
    # que desea modificar?
    # supongamos que el nombre
    nombre = input("Ingrese el nombre nuevo: ")
    with open(TABLA_CLIENTES, "r") as f:
        lines = f.readlines()
    with open("prueba.txt", "w") as f:
        for line in lines:
            if line.strip("\n").split(';') != cliente:
                f.write(line)
            if line.strip("\n").split(';') == cliente:
                f.write(f'3;{nombre};11;23;230323;0%;0\n')
    print("Cliente modificado")
# modificarCliente(getCliente("id", getClientes()))


# Funcion para verificar si el id del cliente existe, si no existe, retorna el valor del id
def clienteExist():
    encontrado = False

    idCliente = input("Ingrese el id del cliente: ")
    for cliente in getClientes():
        if cliente[0] == idCliente:
            encontrado = True
    
    if encontrado == True:
        print("ID de cliente ya existe, ingrese otro")
        return clienteExist()

    else:
        return idCliente
    
# funcion para retornar fecha de visita
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