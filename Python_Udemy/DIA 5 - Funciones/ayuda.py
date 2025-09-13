dic = {'clave1': 100, 'clave2': 500}

a = dic.popitem()

print(a)
print(dic)

# Ejercicio 2

a = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

# este metodo funiciona para elimiar caracteres especificos, como espacios en blanco
b = a.strip(", : % _ # ")
for elemento in b:
    if elemento == "%":
        elemento = "h"
    print(b)


# Ejercicio 3

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

# isdisjoint verifica si ambas listas contienen elementos en comun
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)


print(conjuntos_aislados)
