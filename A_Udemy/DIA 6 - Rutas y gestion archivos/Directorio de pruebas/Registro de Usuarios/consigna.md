Construir un programa que permita:

    Registrar nuevos usuarios con nombre de usuario y contraseña segura.

    Guardar los datos en un archivo (usuarios.txt).

    Evitar registros duplicados (mismo nombre de usuario).

    Permitir que un usuario inicie sesión validando su contraseña.

    Mostrar un mensaje si la contraseña es incorrecta o el usuario no existe.

🧩 Requisitos técnicos:

    Guardar en el archivo:

    usuario:juan | hash:3f8d930a... | fecha:2025-05-17 15:42

    Las contraseñas no deben guardarse en texto plano, sino como hash (una codificación no reversible).

    El usuario puede elegir entre:

        [1] Registrarse

        [2] Iniciar sesión

        [3] Salir

🧠 Lo que debes investigar y aplicar tú:
Qué debes hacer	Qué buscar / investigar
Guardar fecha y hora	datetime.now().strftime(...)
Encriptar contraseña	Módulo hashlib, función sha256()
Leer y escribir líneas en archivos	open(..., "r"), readlines(), split()
Evitar usuarios repetidos	Leer archivo y buscar si el nombre ya existe
Comparar hashes al hacer login Convertir la contraseña ingresada al mismo hash
💡 Tip:

Hazlo modular: crea funciones como:

    registrar_usuario()

    login_usuario()

    validar_contraseña_segura()

📌 Resultado esperado:

Bienvenido al sistema
1. Registrarse
2. Iniciar sesión
3. Salir
Opción: 1

Nombre de usuario: juan
Contraseña: Hola1234

✔ Registro exitoso

...
