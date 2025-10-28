import re,os,time
from  math import ceil;
from colorama import init,Fore,Back,Cursor;
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# Alternativa
# rutaDirectorio = os.path.join(os.path.dirname(__file__), 'Mi_Gran_Directorio')

#rutaerr = 'Python_Udemy/DIA 9 - Mas modulos/Proyecto dia 9/Errorlog.log'# formato de Numero de serie.
#- [N] + [tres carateres de texto] + [-] + [5 números]


rutaDirectorio = Path('Mi_Gran_Directorio')
numero_serie = re.compile(r'(N\w{3})-(\d{5})') # Los separaramos por grupo
conteo = 0
os.system("clear")
def decorador(funcion) -> str:
    # Funcion interna que decora la funcion pasada por parametro
    # Solo es una funcion para decorar, no es la que cuenta el tiempo de ejecucion
    def funcion_interna(*args):
        print("=====================================")
        print("Serial Number Results")
        # solo la formateamos para evitar problemas con el entorno de timeit
        print(f"Search Date: [{datetime.now().strftime('%d/%m/%Y')}]")
        print()
        print("File(s)\t\t Serial No.")
        print("---------------\t ----------")
        inicio = time.time()
        funcion(args[0])
        final = time.time()
        print()
        print(f"• Serial Number's Found: {conteo}")
        print(f"• Search Duration: {ceil(final-inicio)} seconds")
        print()
        print("• Made by LuisD3vv")
        print("=====================================")
    return funcion_interna

@decorador
def hallazgos(ruta):
    # iterar sobre la estructura de carpetas del directorio
    archivos = defaultdict(int)
    try:
        if not os.listdir(ruta):
            print("The directory is empty")
        else:
            for directorio, _, archivo in os.walk(ruta):
                ...
                for arch in archivo:
                    # Utilizamos join para unir las rutas y sus archivos, asi evitamos perder la ruta donde estaba el arcvivo que se esta leyendo actualmente
                    actual = os.path.join(directorio,arch)
                    with open (actual) as lect:
                        for coincidencia in re.finditer(numero_serie,lect.read()):
                            archivos[arch] = coincidencia.groups()
            for clave,valor in archivos.items():
                archivo, serie = valor
                global conteo
                conteo += 1
                
                print(f"| {clave}\t {archivo}-{serie} |")
    except FileNotFoundError as File:
        print(File)
    return conteo

if not os.path.exists(rutaDirectorio):
    print("The given path doesn't exists.")
else:
    hallazgos(rutaDirectorio)



# Decorando la salida de la funcion, para una mejor funcio





