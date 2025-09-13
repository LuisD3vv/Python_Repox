from datetime import datetime

"""
para evitar confusiones
datetime.date -> solo fechas
datetime.time -> solo hora
datetime.datetime -> fecha + hora (si, la clase para manejarlos a ambos se llama igual qu el modulo)
datetime.timedelta -> direfencias de tiempo
datetime.timezone -> para manejar zonas horarias
"""


# sistema de 24 horas
mi_hora = datetime.time(17, 35, 59, 1500)
"""
# fecha
mi_dia = datetime.date(2025, 10, 17)
print(mi_dia.year)
print(mi_dia.month)
print(mi_dia.day)
print(mi_dia.ctime())  # con formato completo
print(mi_dia.today())"""

print(mi_hora)
print(mi_hora.minute)
print(repr(mi_hora))
print(type(mi_hora))

"""
mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
mi_fecha = mi_fecha.replace(month=11) # reemplazar elemento
print(mi_fecha)
"""
"""nacimiento = date(1995,3,5)
muerte = date(2025,6,19)
vida = muerte-nacimiento
print(vida)"""

depierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
vigilia = duerme-depierta
print(vigilia.seconds)
