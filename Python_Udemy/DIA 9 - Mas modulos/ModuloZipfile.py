import zipfile

# hay que tener cuidado con los espacios en los nombres


#nombre del archivo zip y el modo de apertura
with zipfile.ZipFile('archivo_comprimido.zip', 'w') as mi_zip:
    #Nombres de los archivos a comprimir
    mi_zip.write('mi_texto_A.txt')
    mi_zip.write('mi_texto_B.txt')


# #cerrar el archivo
# #mi_zip.close()

# para decomprimir el archivo
with zipfile.ZipFile('archivo_comprimido.zip', 'r') as zip_abierto:
    zip_abierto.extractall()