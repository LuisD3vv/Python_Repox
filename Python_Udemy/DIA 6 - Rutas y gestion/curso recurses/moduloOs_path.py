import os

ruta = os.path.join(os.path.dirname(__file__),'mi_archivo.txt')

'''
2
os.getcwd() → directorio de trabajo actual.

os.chdir(path) → cambiar directorio de trabajo.

os.environ → mapping con variables de entorno (dict-like).

os.getenv('VAR', default=None) → leer variable de entorno.

os.putenv('VAR', 'valor') → establecer variable (mejor usar os.environ['VAR']='valor').
'''

'''
3. Manipulación de directorios

os.listdir(path='.') → lista nombres (archivos y carpetas).

os.scandir(path='.') → iterador con DirEntry (más eficiente).

os.mkdir(path, mode=0o777) → crea un directorio (falla si ya existe).

os.makedirs(path, exist_ok=False) → crea árbol de directorios; exist_ok=True no falla si existe.

os.rmdir(path) → elimina un directorio vacío.

os.removedirs(path) → elimina recursivamente directorios vacíos.

'''

'''
4. Manipulación de archivos

os.remove(path) / os.unlink(path) → elimina archivo.

os.rename(src, dst) → renombrar o mover.

os.replace(src, dst) → reemplaza atomically (sobrescribe si existe).

os.stat(path) → os.stat_result con metadata (size, mtime, mode, uid, gid...).

os.chmod(path, mode) → cambiar permisos.

os.chown(path, uid, gid) → cambiar dueño (Unix).

'''

'''

5. Iterar estructura de directorios

os.walk(top, topdown=True) → genera (root, dirs, files) recursivamente.

Ejemplo rápido:

for root, dirs, files in os.walk('mi_carpeta'):
    for f in files:
        print(os.path.join(root, f))
'''
'''
6. Rutas con os.path (o pathlib como alternativa moderna)

os.path.join(a, *parts) → une componentes de ruta correctamente.

os.path.exists(path) → True si existe (archivo o directorio).

os.path.isfile(path) → True si existe y es archivo.

os.path.isdir(path) → True si existe y es directorio.

os.path.isabs(path) → True si es absoluta.

os.path.abspath(path) → ruta absoluta.

os.path.realpath(path) → ruta real resolviendo symlinks.

os.path.relpath(path, start=os.curdir) → ruta relativa desde start.

os.path.basename(path) → nombre final (archivo/dir).

os.path.dirname(path) → directorio padre.

os.path.split(path) → (dir, base).

os.path.splitext(path) → (raiz, ext).

os.path.normpath(path) → normaliza (quita .., .).

os.path.normcase(path) → normaliza mayúsculas/minúsculas según SO.

os.path.getsize(path) → tamaño en bytes.

os.path.getmtime(path) → última modificación (timestamp).

os.path.samefile(a, b) → True si apuntan al mismo inode (Unix).
'''
'''

7. Constantes útiles

os.sep → separador de ruta ('/' o '\\').

os.pathsep → separador en $PATH (':' o ';').

os.linesep → separador de línea del sistema.

os.name → nombre simple del sistema ('posix', 'nt').
'''
'''

8. Ejecutar procesos

Consejo: usa subprocess para control fino; os.system() es simple pero limitado.

os.system(cmd) → ejecuta comando (retorna código de salida).

os.execv(path, args) / os.execvp(prog, args) → reemplaza proceso actual (avanzado).

os.spawn* → variantes para crear procesos (menos comunes que subprocess).
'''
'''

9. Información del proceso (Unix/General)

os.getpid() → pid actual.

os.getppid() → pid padre.

os.getuid(), os.getgid() → uid/gid (Unix).

os.setuid(uid), os.setgid(gid) → cambiar identidad (privilegios).

os.umask(mask) → obtener/establecer máscara de permisos.
'''
'''
10. Enlaces simbólicos

os.symlink(src, dst) → crear symlink (permiso requerido en Windows <10).

os.readlink(path) → leer destino de symlink.
'''
'''
11. Buenas prácticas y recomendaciones

Para copiar archivos usa shutil.copy o shutil.copy2 (preserva metadata).

Para operaciones atómicas (mover/renombrar seguro) usa os.replace o tempfile + os.replace.

Para rutas modernas y legibles, considera pathlib.Path (más orientado a objetos).

Evita os.system si necesitas capturar salida; usa subprocess.run(...).

Usa os.scandir() cuando iteres muchos archivos (es más rápido que listdir).

Maneja excepciones (FileNotFoundError, PermissionError, OSError) en operaciones de I/O.
'''
'''

12. Ejemplos prácticos

Crear carpeta si no existe:

os.makedirs('data/inputs', exist_ok=True)

Listar solo archivos con cierta extensión:

for entry in os.scandir('mi_dir'):
    if entry.is_file() and entry.name.endswith('.csv'):
        print(entry.path)

Mover y renombrar (sobrescribir si existe):

os.replace('tmp/archivo.txt', 'data/archivo_final.txt')

Obtener tamaño y fecha modificada legible:

st = os.stat('archivo.bin')
print('bytes:', st.st_size)
print('modificado:', datetime.fromtimestamp(st.st_mtime))
'''