numero = 2000.42
numerito = 1500.736

resultado = numero + numerito
resultado = round(resultado, 2)
print(resultado)
# ----------

# El redondeo funciona dependiendo de la cercania del decimal con el proximo numero

resultado = round(90/7)
redondeo = round(resultado)

print(resultado)

valor = 95.666666666666
# round require don parametros, el numero o variable y la canitdad de digitos depues del cero
print(round(valor, 2))
