# Funcion para obtener la lista de clientes
def getClientes():
    listaClientes = []
    archivo = open('database/clientes.txt')
    for linea in archivo.readlines():
        listaClientes.append(linea.replace("\n", "").split(';'))

    # print(listaClientes)
    return listaClientes
# getCliente()


# Funcion para buscar un cliente por id
def getCliente(idCliente, listaClientes):
    for cliente in listaClientes:
        if cliente[0] == idCliente:
            # print(cliente)
            return cliente
    print("No se encontro el cliente")
    return False
# getCliente("id", getClientes())


# Funcion para eliminar un cliente de la base de datos
def deleteCliente(cliente):
    if cliente == False:
        return False
    with open("database/clientes.txt", "r") as f:
        lines = f.readlines()
    with open("prueba.txt", "w") as f:
        for line in lines:
            if line.strip("\n").split(';') != cliente:
                f.write(line)
    print("Cliente eliminado")
# deleteCliente(getCliente("id", getClientes()))


# Funcion para agregar un cliente
def addCliente():
    # id autoincremental? || hacer funcion para actualizar los ids || o obtener ultimo id
    # cedula?
    time = "" # importamos una libreria para obtener el dia
    idCliente = input("Ingrese el id del cliente: ")
    nombreCliente = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese el direccion del cliente: ")
    ciudad = input("Ingrese el ciudad del cliente: ")
    telefono = input("Ingrese el telefono del cliente: ")
    fecha = time
    descuento = input("Ingrese el porcentaje de descuento para el cliente: ")
    saldo = input("Ingrese el saldo a deber del cliente: ")
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
    with open("database/clientes.txt", "r") as f:
        lines = f.readlines()
    with open("prueba.txt", "w") as f:
        for line in lines:
            if line.strip("\n").split(';') != cliente:
                f.write(line)
            if line.strip("\n").split(';') == cliente:
                f.write(f'3;{nombre};11;23;230323;0%;0\n')
    print("Cliente modificado")
# modificarCliente(getCliente("id", getClientes()))