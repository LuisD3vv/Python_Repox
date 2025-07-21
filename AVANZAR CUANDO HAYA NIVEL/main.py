from os import system
from gestor_libros import Libro
from gestor_usuarios import Usuario
from gestor_prestamos import Prestamo
# from datetime import datetime 
from pathlib import Path
from gestor_libros import agregar_libro
import time

def validar_titulo(titulo):
    groserias = ['verga',
                'culo','puta'
                'perra','pinche',
                'pendejo',
                'puto,basura','mierda','vagina',
                'pene']
    
    for badw in groserias:
        if badw in titulo:
            print("Titulo con contenido mal sonante")
            return f"incorrecto {badw}"
        elif len(titulo) < 4:
            print(f"Titulo demaciado corto {len(titulo)}")
            return "incorrecto"
    return "correcto"

def validar_autor(autor):
    groserias = ['verga','culo','puta'
                'perra','pinche','pendejo',
                'puto,basura','mierda','vagina',
                'pene']
    for badw in groserias:
        if badw in autor:
            print("Titulo con contenido mal sonante")
            return f"incorrecto {badw}"
        elif len(autor) < 4:
            print(f"Titulo demaciado corto {len(autor)}")
            return "incorrecto"
    return "correcto"

def validar_fecha(fecha):
    sep = fecha.split("-")
    print(sep)
    dia, mes, anio = sep
    # print(f"Valores logicos fechas en bruto {lengdia} {lengmes} {lenganio1}")
    if len(anio) > 4:
        print("El año debe de tener 4 digitos")
        return "mal formato año"
    elif 3 < len(mes) < 2:
        print("El mes debe de tener 2 digitos y con formato 00")
        return "mal formato mes"
    elif len(dia) > 2:
        print("El dia debe de tener 2 digitos")
        return "mal formato dia"
    else:
        no1 = int(dia) > 0 or int(dia) < 31
        no2 = int(mes) < 12 or int(mes) > 0
        no3 = int(anio) < 2999 and int(anio) > 0000
        print(f"Valor logico fechas => {no1} | {no2} | {no3}")
        if (no1 and no2 and no3 == True):
            return "correcto"
        else:
            return "aun hay errores"
            print(f"Log de validacion en {no1}-{no2}-{no3}")
        return sep

def validar_genero(genero):
    groserias = ['verga','culo','puta'
                'perra','pinche','pendejo',
                'puto,basura','mierda','vagina',
                'pene']
    for badw in groserias:
        if badw in genero:
            print("Titulo con contenido mal sonante")
            return f"incorrecto {badw}"
        elif len(genero) < 4:
            print(f"Titulo demaciado corto {len(genero)}")
            return "incorrecto"
    return "correcto"

def validar_editorial(editorial):
    groserias = ['verga','culo','puta'
                'perra','pinche','pendejo',
                'puto,basura','mierda','vagina',
                'pene']
    for badw in groserias:
        if badw in editorial:
            print("Titulo con contenido mal sonante")
            return f"incorrecto {badw}"
        elif len(editorial) < 4:
            print(f"Titulo demaciado corto {len(editorial)}")
            return "incorrecto"
    return "correcto"
# Se modularizo el codigo para hacer mas optimo el codigo y poder probar cada parte por separado

def agregar_libros():
    print("Cargando...")
    time.sleep(2)
    system("clear")
    print("listo!")
    print("Menu de elementos para ingresar libros(-1 para salir): ")
    print("Ingresa los siguiente:")
    while True:
        libro_nombre = input("Titulo: ")
        libno = validar_titulo(libro_nombre)
        if libno != "correcto":
            print("Incorrecto, intenta de nuevo")
            continue
        libro_autor = input("Autor: ")
        valal = validar_autor(libro_autor)
        if valal != "correcto":
            print("Incorrecto, intenta de nuevo")
            continue
        while True:
            try:
                libro_fecha = input("Fecha de lanzamiento [-DD-MM-YYYY-]: ")
                valfech = validar_fecha(libro_fecha)
                print(f"Valor de funcion {valfech}")
            except:
                print("Escribe la fecha en el formato correcto")
            else:
                
                if valfech == "correcto":
                    break
                else:
                    continue
        libro_genero = input("Genero: ")
        valgen = validar_genero()
        libro_editorial = input("Editorial: ")
        valedit = validar_editorial(libro_editorial)
        
        correcto = (libno,valal,valfech,valgen,valedit )= "correcto"
        if correcto:
                print("Enviando datos")
                agregar_libro(autor=libro_nombre,titulo=libro_nombre,editorial=libro_editorial,fecha=libro_fecha,genero=libro_genero)
                break
        elif not correcto:
            print(f"Outuput log - nombre: {libno} | autor {valal} | fecha {valfech}")
        else:
            continue
def registrar_usuario():
    ...
def prestamo_libro():
    print("Has seleccionado prestar libro")
    print("Para realizar un prestamo es necesario estar registrado con una id.")
def mostrar_libros_disponibles():
    ...
def buscar_Libro():
    system("clear")
    print("Buscar por\n1. Autor\n2. Nombre\n3. Genero")
    busqueda = int(input("Eleccion: "))
    """
    Buscar por nombre, autor y genero
    """
def salir():
    ...
#Interfaz base
def main():
    system("clear")
    while True:# Sistema de gestion internacional de biblioteca
        print("Bienvenido al -SDGIB-")
        print("1. Agregar Libro\n2. Registrar usuario\n3. Pedir un Libro\n4. Libros disponibles\n5. Buscar Libro\n6. Salir")
        while True:
            try:
                opcion = int(input("Que deseas realizar?: "))
            except ValueError as e:
                system("clear")
                print(f"Opcion entera incorrecta => error [|{e}|]")
            else:
                break
        print(f"La opcion elegida es {opcion}")
        match opcion:
            case 1: agregar_libros()
            case 2: registrar_usuario()
            case 3: prestamo_libro()
            case 4: mostrar_libros_disponibles()
            case 5: buscar_Libro()
            case 6: salir()
            case _:
                print("Ha ocurrido un error inesperado")
#LLamar a la funcion principal
main()
# Probar funciones por separado
# while True:
#     try:
#         print("Ingresa una fecha")
#         fech = input("fecha = [-DD-MM-YYYY-]:")
#     except:
#         print("ERROR")
#     else:
#         if validar_fecha(fech) == "correcto":
#             break
#         else:
#             continue
# print(validar_fecha(fech))
