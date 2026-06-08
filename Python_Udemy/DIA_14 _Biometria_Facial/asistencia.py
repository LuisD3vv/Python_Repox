from cv2 import imread,cvtColor,COLOR_BGR2RGB,VideoCapture,CAP_DSHOW,imshow,waitKey,rectangle,putText,FILLED,FONT_HERSHEY_COMPLEX
import face_recognition as fr
import os
import numpy 
from datetime import datetime

#* crear base de datos
ruta = '/home/lissandro/Python_Repox/Python_Udemy/DIA_14 _Biometria_Facial/Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)


for nombre in lista_empleados:
    imagen_actual = imread(f'{ruta}/{nombre}') # error de ruta
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])
print(nombres_empleados)

#* Codificar imagenes
def codificar(imagenes):
    
    #* Crear una lista nueva
    lista_codificada = []
    
    #* pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cvtColor(imagen,COLOR_BGR2RGB)
        
        #* codificar
        codificado = fr.face_encodings(imagen)[0]
        
        #* Agregar a la lista
        lista_codificada.append(codificado)
        
    #* devolver lista codificada
    return lista_codificada

# registrar los ingresos
def registrar_ingresos(persona):
    f = open('registros.csv','r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(",")
        nombres_registro.append(ingreso[0])
    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

lista_empleado_codificada = codificar(mis_imagenes)

#* Tomar una imagen de camara
captura = VideoCapture(0,CAP_DSHOW)

#* Leer la imagen de la camara
exito,imagen = captura.read()
if not exito:
    print("no se ha podido tomar la captura")
else:
    #* reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    
    #* codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen,cara_captura)
    
    #* buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada,cara_captura):
        coincidencias = fr.compare_faces(lista_empleado_codificada,caracodif)
        distancias = fr.face_distance(lista_empleado_codificada,caracodif)
        
        # * mostrar la coincidencia
        indice_coincidencia = numpy.argmin(distancias) # almacena el menor
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados.")
        else:
            # * buscar el nombre del empleado encontrado]
            nombre = nombres_empleados[indice_coincidencia]
            
            y1,x2,y2,x1 = caraubic
            rectangle(imagen,(x1,y1),(x2,y2),(0,255,0),2)
            rectangle(imagen,(x1, y2 - 35),
                    (x2,y1),
                    (0,255,0),
                    FILLED)
            putText(imagen,nombre,(x1+6,y2-6),FONT_HERSHEY_COMPLEX,1(255,255,255),2)


            registrar_ingresos(nombre)
            
            # * mostrar la imagen obtenida
            imshow('Imagen web',imagen)
            
            #* mantener  ventana abierta
            waitKey(0)