"""
Lissandro AG 06/01/2025
"""

def devolver_distintos(a,b,c):
    suma = list()
    suma.append(a)
    suma.append(b)
    suma.append(c)
    resultado = sum(suma, start=0)

    if resultado > 15:
        print(max(f" el mayor {suma}"))
    elif resultado < 10:
        print(min(f" el menor {suma}"))
    elif 10 <= resultado <= 15:
        print(suma)
    else:
        print("okey")



numeros = devolver_distintos(90,90,90)
