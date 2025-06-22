from datetime import datetime
from pathlib import Path
#Log de registro seguro

""" 
Objetivo:

Construir un sistema que:
Pida el nombre del usuario y su contraseña.
Valide la contraseña (mín. 8 caracteres, mayúscula, minúscula, número).
Si es válida:
La guarda junto con el nombre en un archivo registro.txt.
Registra la fecha y hora del registro (log).
Si es inválida:
Muestra mensajes de error y vuelve a pedir los datos.
"""
ruta = Path.home()  / "Python_Repox" / "Code" / "DIA6" / "Directorio de pruebas" / "Log de contraseñas" / "log" / "ingresos_2025.txt"

def es_valida(contra):
    mayusculas = any(c.isupper() for c in contra)
    minusculas = any(c.islower() for c in contra)
    numeros = any(c.isnumeric() for c in contra)

    if len(contra) < 8:
        return "Al menos necesitas 8 caracteres"

    if not mayusculas:
        print("❌ ingresa almenos una mayuscula")
    else:
        print("Mayuscula ✔")

    if not minusculas:
        print(" ❌ ingresa al menos una minuscula")
    else:
        print("Minuscula ✔")

    if not numeros:
        print(" ❌ Ingresa al menos un numero")
    else:
        print("Numero ✔")

    if mayusculas and minusculas and numeros:
        return "contraseña valida"
    else:
        return "contraseña invalida"

usuario = input("ingresa tu usuario: ")

while True:
    contra = input("Ingresa tu contraseña: ")
    correcto = es_valida(contra)
    print(correcto)
    if correcto == "contraseña valida":
        print(f"Access grated {usuario}")
        with open(ruta, "a") as archivo:
            inversa = contra[::-1]
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # objeto traido de la libreria datetime, se requiere trabajarlo como string
            archivo.write(f"User: {usuario} | Password: {inversa} (Encrypted) | Date: {str(fecha)}\n\n")
        break