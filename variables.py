TABLA_CIUDADES = "database/Ciudades.txt"
TABLA_CLIENTES = "database/Clientes.txt"
TABLA_PAISES = "database/Paises.txt"
TABLA_MASCOTAS = "database/Mascotas.txt"
TABLA_VISITAS = "database/Visitas.txt"
TABLA_TRATAMIENTOS = "database/Tratamiento.txt"
TABLA_MEDICACION = "database/Medicacion.txt"

LISTA_PAISES = []
LISTA_CIUDADES = []
LISTA_CLIENTES = []
LISTA_MASCOTAS = []
LISTA_VISITAS = []
LISTA_TRATAMIENTOS = []
LISTA_MEDICACION = []

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
    return [dia,mes,ano]