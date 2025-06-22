def multiplicar(numero1, numero2):
    return numero1 * numero2  # un return puede ser utilizado para guardar la infomacion en una variable y no solo imprimir el resultado como seria utilizando print


resultado = multiplicar(6, 8)  # aqui se guarda
print(resultado)


def usd_a_eur(monto):
    euros = monto * 0.9
    return euros


dolares = 5
conversion = usd_a_eur(dolares)
print(conversion)


# Se define una función llamada invertir_palabra que toma un parámetro llamado palabra.
def invertir_palabra(palabra):
    # Se convierte la palabra a mayúsculas usando el método upper(). La conversión de la cadena a una lista de caracteres (list(palabra)) se realiza para facilitar la inversión de la cadena. En Python, las cadenas son inmutables, lo que significa que no puedes modificar directamente los caracteres de una cadena. Sin embargo, puedes trabajar con listas, que son mutables.
    cadena_invertida = list(palabra.upper())
    cadena_invertida.reverse()  # La lista se invierte con el método reverse().
    # Finalmente, se une la lista invertida de nuevo en una cadena con join().
    resultado = ''.join(cadena_invertida)
    # La función devuelve la cadena invertida y en mayúsculas.
    return resultado


# Se define una variable llamada palabra con el valor 'Curso'.
palabra = 'Curso'
# Se llama a la función invertir_palabra con palabra como argumento y el resultado se guarda en cadena_resultado.
cadena_resultado = invertir_palabra(palabra)
print('Palabra original', cadena_resultado)  # se imprime la cadena original
# Se imprime la palabra invertida y se convierte a mayúsculas usando upper() para reflejar el mensaje correctamente.
print('Palabra invertida y en mayuscula:', cadena_resultado.upper())
