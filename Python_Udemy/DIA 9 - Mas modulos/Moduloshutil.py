import shutil
# no nombrar los archivos igual que los modulos


# carpeta_origen = '/home/lissandro/Escritorio/Proyecto Horus'

# # para comprimir
# archivo_destino = 'Todo_Comprimido'

# # para crear un archivo zip
# # nos pide archivo destino, algoritmo y destino
# shutil.make_archive(archivo_destino,'zip',carpeta_origen)



# Descomprimir usando shutil

shutil.unpack_archive("Todo_Comprimido.zip",'Todo_descomprimido','zip')








