from cv2 import COLOR_BGR2RGB,cvtColor,imshow,waitKey,rectangle,putText,FONT_HERSHEY_COMPLEX

import face_recognition as fr


#* Cargar imagenes
foto_control = fr.load_image_file('img/FotoA.jpg')
foto_prueba = fr.load_image_file('img/FotoC.jpg')

#* pasar imagenes a rgb
foto_control = cvtColor(foto_control,COLOR_BGR2RGB)
foto_prueba = cvtColor(foto_prueba,COLOR_BGR2RGB)

#* localizar cara control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

#* localizar cara control
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]


#* Mostrar donde se encuentra la cara (rectangulos)
rectangle(foto_control,
        (lugar_cara_A[3],lugar_cara_A[0]),
        (lugar_cara_A[1],lugar_cara_A[2]),
        (0,255,0),
        2)

rectangle(foto_prueba,
        (lugar_cara_B[3],lugar_cara_B[0]),
        (lugar_cara_B[1],lugar_cara_B[2]),
        (0,255,0),
        2)

#* realizar comparacion /  se puede modificar la sensibilidad a la igualdad.
resultado = fr.compare_faces([cara_codificada_A],cara_codificada_B,)
#* imprimir el resultado booleano de parentezco


#* mostrar distancia
distancia = fr.face_distance([cara_codificada_A],cara_codificada_B)

#* mostrar resultado formateado con texto y colores
putText(foto_prueba,
        f"{resultado} {distancia.round(2)}",
        (50,50),
        FONT_HERSHEY_COMPLEX,
        1,
        (0,255,0),
        2)

#* mostrar imagenes
imshow('Foto Control',foto_control)
imshow('Foto Prueba',foto_prueba)

#* mantener el programa abierto
waitKey(0)