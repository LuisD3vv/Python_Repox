print("------------------Buenas Tardes-----------------")
print("Bienvenido al sistema de comisiones de sarscov\npara empezar, Cual es tu nombre")
nombre = input("¿Cual es tu nombre?: ")
ventas = int(input("Ingresa las ventas que tuviste este mes: "))
comision = 0.25 # muy alta

comision_final = round(ventas * comision, 2)
print(f'Hola {nombre} tu comision miserable, basada en tus ventas {ventas} es de ${comision_final}')

# comision ventas * 13% /100, 2
# preguntar nombre y ventas
