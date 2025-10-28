from pathlib import Path
import os

ruta = Path("Mi_Gran_Directorio")
rutados = Path("Errorlog.log")
if not Path.exists(rutados):
    print("no existe la ruta")
else:
    with open (rutados,"r") as lect:
        print(lect.read())
