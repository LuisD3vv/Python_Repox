# Codigo hecho por Luis Alejandro Aguilar Soberanes

# importando el dataset
import pandas as pd
from ventas import ventas 

# convertir el archivo en un dataset
df = pd.DataFrame(ventas)


print("Productos con ventas mayores a $500")
for venta in ventas:
    if venta['precio'] * venta['cantidad'] > 500:
        print(f"{venta['producto']} Ventas: ${venta['precio'] * venta['cantidad']}")
        
print()
# el producto mas economico y el mas barato
nombre_mayor = df.loc[df['precio'].idxmax(),"producto"]
nombre_menor = df.loc[df['precio'].idxmin(),"producto"]

mayor = df['precio'].max()
menor = df['precio'].min()
print(f"Producto mas Economico: {nombre_mayor} ${mayor}")
print(f"Producto mas Costoso: {nombre_menor} ${menor}")

# Productos de la categoria tecnologia

print()
for venta in ventas:
    if venta['categoria'] == "Centro":
        print(venta['producto'])