mascota = 'perro'

if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'Conejo':
    print('Tienes un conejo')
else:
    print('No se que animal tienes')


edad = 16
calificacion = 9

if edad < 18:
    print('eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('no aprobaste')
else:
    print('eres adulto')