from os import system

system("clear")
def suma():
    n1 = int(input("Numero uno: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print("Gracias por sumar")

# Mannejo de excepiones
try:
    #codigo que queremos probar
    suma()
except TypeError: 
    # codigo a ejecutar si hay error
    print("No es posibe concatenar variables int mas str")
except ValueError:
    print("No es el tipo de dato esperado")
else:
    # Se ejecuta si no hay un error
    print("Todo salio bien")
finally:
    #codigo a ejecutar siempre
    print("Pene")

"""Hay bastantes tipos de errores, 
es recomendable nvestigar para hacer un codigo mas rico
y protegido 
de los mas conodicos 
nombres mal escritos pero se entiende la idea
typerror / tipo de dato incorrecto
ValueError / tipo correcto, valor inadecuado
zeroDivsionError / divison por cero
syntax error / codigo mal escrito
indentation error / error de indentacion(espacios en lugar de tabulaciones)
name error / error en el nombre de la variable
index error / indice fuera de la lista
key error / clave que no existe en un diccionario
atribute error / metodo o atributo que no exite para un objeto determinado
filenotfounerror / intentar abrir un archivo que no existe
osError / ioerror  / abrir archivos mal cerrado o falta de permisos
"""

def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")
    
    
pedir_numero()

#Ejercicios de manejo de errores
"""
Implementa para la siguiente función suma(), 
un manejador de errores simple que ante cualquier error, 
imprima en pantalla el mensaje: "Error inesperado". 
En caso contrario, deberá limitarse a mostrar
el resultado de la suma entre los dos números.
"""

def suma(num1,num2):
    """Funcion basica de suma"""
    try:
        num1 + num2
    except:
        print("Error inesperado")
    else:
        print(num1+num2)



def cociente(num1,num2):
    """Funcion para probar dos tipos de errores comunes"""
    try:
            (num1/num2)
    except TypeError:
            print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("No se puede dividir entre 0.")
    else:
        print(num1/num2)
cociente(39,0)

# Error FileNotFound
def abrir_archivo(nombre_archivo):
    try:
        with open(nombre_archivo) as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except FileExistsError:
        print("El archivo existe")
    except TypeError:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

# Bascicamente es en pseudopcodigo



"""
Intenta hacer esto, si hay una exepcion de este tipo, haz esto, si no hay anda entonces haz lo normal

"""
