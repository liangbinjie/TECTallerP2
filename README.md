# TECTallerP2
Proyecto 2 TEC Taller IC1803
Binjie Liang

## MANUAL DE USUARIO

Para el uso de esta aplicacion, despues de extraer los archivos, si deseas usar tu propia base de datos, primero eliminar los que hay en la carpeta `database` y agregar los que usted necesite

El formato de cada tabla de datos en archivo de texto varia, ya que hay diferentes tipos de datos, en el siguiente apartado hablaremos de la estructura de cada tabla

## Pseudocodigos
### Algoritmo para agregar
```
Function nombreFuncion() {
    var id = input();
    
    if object(id) == Existe {
        print("Este dato ya existe")
        return False
    }

    var nombreVar = input();

    with open(archivo, "a") as f {
        nuevo = id + nombreVar
        f.write(nuevo)
    }
}