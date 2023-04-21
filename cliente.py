from ciudad import ciudadExist, getCiudad
from pais import paisExist
from variables import TABLA_CLIENTES, LISTA_CLIENTES, fechaV

# Funcion para obtener la lista de clientes apartir del txt
def cargarClientes():
    listaClientes = []
    archivo = open(TABLA_CLIENTES)
    for linea in archivo.readlines():
        listaClientes.append(linea.replace("\n", "").split(';'))

    for cliente in listaClientes:
        if cliente not in LISTA_CLIENTES:
            LISTA_CLIENTES.append(cliente)


# Funcion para buscar un cliente por id
def getCliente(idCliente):
    for cliente in LISTA_CLIENTES:
        if cliente[0] == idCliente:
            # print(cliente)
            return cliente
    print("No se encontro el cliente")
    return False

# Funcion para agregar un cliente
def addCliente():
    idCliente = clienteExist() # verificar que no este repetido
    nombreCliente = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese el direccion del cliente: ")
    pais = str(int(input("Ingrese el codigo del pais: ")))
    while paisExist(pais) == False:
        print("Este pais no existe en la base de datos, intente con otro")
        pais = str(int(input("Ingrese el codigo del pais: ")))
    ciudad = str(int(input("Ingrese el codigo de la ciudad: ")))
    infoCiudad = getCiudad(ciudad)
    while ciudadExist(ciudad) == False or not infoCiudad[0] == pais: # mientras que la ciudad no exista en la base de datos
        print("Esta ciudad no existe en la base de datos, o no pertenece a su respectivo pais")
        ciudad = str(int(input("Ingrese el codigo de la ciudad: ")))
        infoCiudad = getCiudad(ciudad)
    telefono = str(int(input("Ingrese el telefono del cliente: ")))
    fecha = fechaV()
    descuento = str(int(input("Ingrese el porcentaje de descuento para el cliente: ")))
    saldo = str(int(input("Ingrese el saldo a deber del cliente: ")))
    nuevo = [idCliente, nombreCliente, direccion, pais, ciudad, telefono] + fecha + [descuento, saldo]
    LISTA_CLIENTES.append(nuevo)
    print("Cliente nuevo agregado")

# Funcion para verificar si el id del cliente existe, si no existe, retorna el valor del id
def clienteExist():
    encontrado = False

    idCliente = str(int(input("Ingrese el id del cliente: ")))
    for cliente in LISTA_CLIENTES:
        if cliente[0] == idCliente:
            encontrado = True
    
    if encontrado == True:
        print("ID de cliente ya existe, ingrese otro")
        return clienteExist()

    else:
        return idCliente

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



# Funcion para modificar el cliente
def modificarCliente(cliente):
    if cliente == False:
        return False
    
    opcion = input("Que desea modificar?\n[1]ID\n[2]Nombre\n[3]Direccion\n[4]")
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
