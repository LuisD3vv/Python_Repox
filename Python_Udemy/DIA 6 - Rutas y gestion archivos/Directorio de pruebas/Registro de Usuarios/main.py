from datetime import datetime # importar modulo de fecha y tiempo.
from pathlib import Path # Crear rutas
#from hashlib import sha256 # Simular encriptacion 
#Sha256 es el algoritmo de encriptacion a la verga mi perro
import bcrypt # encriptacion real pues a la verga

ruta = Path("A_Udemy/DIA 6 - Rutas y gestion archivos/Directorio de pruebas/Registro de Usuarios/usuarios.txt")
print(ruta)
#Validar contraseña
def validar_contraseña_segura(contra):
    mayusculas = any(letra.isupper() for letra in contra)
    minusculas = any(letra.islower() for letra in contra)
    numeros = any(letra.isnumeric() for letra in contra)

    if len(contra) < 8:
        print("Al menos necesitas 8 caracteres")
        return 

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
#Validar Que el usuario no este repetido
def validar_usuario(usuario):
    with open(ruta,"r") as verificar:
        for line in verificar:
            if line == "\n":
                continue
            nombre, contrasenia, fecha = line.split("|")
            COnt1 = [] # Usuario real
            i = 6
            while nombre[i] != " ":
                COnt1.append(nombre[i])
                i+= 1
            real = ''.join(COnt1)
            usuarios = f'{usuario}'
            if usuarios == real:
                return "nombre de usuario ya existente"
            else:
                return "Usuario valido"

    return "Usuario valido" # por si no hay ningun valor antes.
# Registrar usuario solo si el usurio ingresado no existe y la contraseña cumple los estandares
def registrar_usuario(usuario, contra):
    encript = bcrypt.hashpw(contra.encode(), bcrypt.gensalt()) # une el valor aleatorio junto con la contraseña codificada
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # transformar en string el objeto date
    with open(ruta,"a") as registrar:
        registrar.write(f"User: {usuario} | Psswd: {encript.decode()} | Date: {str(fecha)}\n\n")
        print("Usuario registrado correctamente")
#Validar entradas del usuario, contraseña y usuario
def log_usuario(usuario, contrasenia):
  encode_comp = contrasenia.strip().encode()
  print(encode_comp)
  with open(ruta,"r") as verificar:
        for line in verificar:
            if line == "\n":
                continue
            nombre, contrasenia, fecha = line.split("|")
            nombre_comp = [] # Usuario real
            contra_comp = []
        i = 6
        while nombre[i] != " ":
            nombre_comp.append(nombre[i])
            i+= 1
            real_nombre = ''.join(nombre_comp)
        j = 8
        while contrasenia[j] != " ":
            contra_comp.append(contrasenia[j])
            j+=1
            real_contra = ''.join(contra_comp).strip().encode()

        if bcrypt.checkpw(encode_comp, real_contra):
            return "Acceso concedido"
        else:
            return "Vuelve a intentar"
#Iniciar loop
while True:
    print("Elige una opcion\n[1] Registrarse\n[2] Iniciar sesion\n[3] Salir")
    opcion = int(input("opcion: "))

    if opcion == 1:
        while True:
            usuario = input("Ingresa el nombre de usuario: ")
            validacion_usuario = validar_usuario(usuario)
            contra = input("Ingresa tu contraseña: ")
            correcto = validar_contraseña_segura(contra)
            if correcto == "contraseña valida" and validacion_usuario == "Usuario valido":
                    registrar_usuario(usuario, contra)
                    print("Usuario registrado con exito")
                    break
    elif opcion == 2:
        print("Has elegido iniciar sesión")
        while True:
            usuario_login = input("Ingresa tu Usuario: ")
            contrasenia_login = input("Ingresa tu contraseña: ")
            validacion = log_usuario(usuario_login,contrasenia_login)
            if validacion == "Acceso concedido":
                print(f"Bienvenido {usuario_login}")
                break
            elif validacion == "Vuelve a intentar":
                print("Ha ocurrido un error no se donde")

    elif opcion == 3:
        print("Salir")
        break
