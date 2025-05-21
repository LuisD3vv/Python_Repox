from datetime import datetime # importar rutas
from pathlib import Path # Crear rutas
from hashlib import sha256 # Simular encriptacion
import bcrypt # encriptacion real pues a la verga
import os

ruta = Path.home() / "Python_Repox" / "Code"/ "DIA6"/ "Directorio de pruebas"/ "Registro de Usuarios" / "usuarios.txt"

with open(ruta, "r") as archivo:
    print(archivo.read())
if Path.is_file(ruta):
    print("hay un archivo")

total = 0
with open (ruta,"r") as listar:
        lista = listar.readlines()
        for user in lista:
            total += 1

print(total)

def registrar_usuario(usuario, contra):
    encript = sha256(contra.encode())
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(ruta,"a") as registrar:
        registrar.write(f"User: {usuario} | Password: {encript} (Encrypted) | Date: {str(fecha)}\n\n")
    ...

def log_usuario(ruta,usuario,contra):
    with open (ruta,"r") as verificar:
        lista = verificar.readlines()
        for user in lista:
            if usuario == user:
                print("Nombre de usuario ocupado")
            

    ...
def validar_contraseña_segura(contra):
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
        
    """
    solamente debe de aceptar la contraseña si es
    mayor a ocho caracteres y contiene misnuculas 
    y almenos una mayuscula
    """
    ...


while True:
    print("Elige una opcion\n[1] Registrarse\n[2] Iniciar sesion\n[3] Salir")
    opcion = int(input("opcion:"))

    if opcion == 1:
        usuario = input("Ingresa el nombre de usuario: ")
        while True:
            contra = input("Ingresa tu contraseña: ")
            correcto = validar_contraseña_segura(contra)
            if correcto == "contraseña valida":
                print("Registro exitoso")
                registrar_usuario(usuario, contra)
                break
        


    elif opcion == 2:
        print("Has elegido iniciar sesión")
        credencial_1

    elif opcion == 3:
        print("has Salido")
        break




