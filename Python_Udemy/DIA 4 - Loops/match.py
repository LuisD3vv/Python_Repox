"""
match en un iterado similar al cswicth de otros lenguajes, a diferencia de que aqui
como tal no ponemos un break en el termino de cada una de las opearaciones

"""
from os import system
# CREACION DE UN CARRITO DE COMPRAS CON MATCH 
print("Bienvenido")
compras = ['Condones','Sabritas','Lubricante','Consoladores']
while True:
    print("1.-Agregar producto\n2.-Eliminar producto\n3.-Ver lista\n4.-Salir")
    try:
        opcion = int(input("Hola, que deseas hacer?: "))
    except:
        print("PORFAVOR INGRESA UN NUMERO")
        
    else:
        match opcion:
            case 1:
                print("Ingresa el nombre del producto")
                try:
                    nombre = input("nombre del nuevo producto: ")
                except:
                    print("algo salio mal")
                else:
                    compras.append(nombre)
                    print(f"Se ha agreado exitosamente {nombre}")
            case 2:
                print("cual vas a eliminar")
                for producto in enumerate(compras):
                    print(producto)
                try:
                    nombre_eliminar = int(input("Nombre del producto que deseas eliminar: "))
                    if nombre_eliminar > len(compras):
                        print("Fuera del rango mamon")
                        continue
                except:
                    print("Porfavor, ingresa el numero.")
                else:
                    compras.pop(nombre_eliminar)
            case 3:
                print("Aqui estan los productos disponibles papu")
                for producto in enumerate(compras):
                    print(producto)
            case 4:
                system("clear")
                print("chao chao perro")
                break
            case _:
                print("Ha ocurrido un pinche error")


# match tambien puede usar dos declaraciones
print("Selecciona una putisima opcion: ")
opcion = input(">> ")	
try:
    opcion = opcion.lower()
except ValueError:
    system("clear")
    print("< Es necesario que ingreses un numero >")
except KeyboardInterrupt:
    print("Saliendo...")
else:
    match opcion: # type: ignore
        case "1" | "leer receta":
            print("!")
        case "2" | "crear receta":
            print("!")
        case "3" | "crear categoria":
            print("!")
        case "4" | "eliminar receta":
            print("!")
        case "5" | "eliminar categoria":
            print("!")
        case "6" | "modificar receta":
            print("!")
        case "7" | "limpiar consola":
            print("!")
        case "8" | "salir":
            system("clear")
            print("Has salido exitosamente.")
            exit()  # Salida logica del codigo

