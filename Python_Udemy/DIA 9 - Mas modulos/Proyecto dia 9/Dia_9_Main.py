import zipfile,re,timeit;
from datetime import datetime;from  math import ceil;from os import system,walk

ruta = 'Mi_Gran_Directorio'
# formato de Numero de serie.
#- [N] + [tres carateres de texto] + [-] + [5 números]
numero_serie = re.compile(r'N(\w{3})-(\d{5})')

system("clear")
def decorador(funcion):
    
    def funcion_interna():
        print("----------------------------------------------------")
        print(f"Fecha de búsqueda: [{datetime.now().strftime("%d/%m/%Y")}]")
        print()
        funcion()
        print()
        print(f"Números encontrados: {...}")
        print(f"Duración de la búsqueda: {...} segundos")
        print("----------------------------------------------------")
    return funcion_interna


# Decorando la salida de la funcion, para una mejor funcion
@decorador
def hallazgos():
    #duracion = ceil(timeit.timeit(...))
    # iterar sobre la estructura de carpetas del directorio
    for directorio, subdirectorio, archivo in walk(ruta):
        print(f"En el directorio {directorio}")
        print("Los subdirectorios son: ")
        for carpeta in subdirectorio:
            print(f"\t{carpeta}")
        print("Contiene los archivos:")
        for arch in archivo:
            print(f"\t{arch}")
            # # entrar en cada archivo y verificar si dento hay alguna linea que coincida
            # if arch.endswith(".txt"):
            #     with open (arch,"r") as archivo:
            #         print(archivo.read())
        print()


# llamamos la funcion igual como simpre, ya esta decorada.
hallazgos()





