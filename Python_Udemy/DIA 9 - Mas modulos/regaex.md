
# Glosario (2 espacios para dar un salto de linea)

>/d digito numerico  
>/w caracter alfanumerico (letras y numeros)  
>/s espacio en blanco  
>/D NO es un digito  
>/W No es alfanumerico (solo signos)  
>/S no es un espacio en blanco  

## cuantificadores

### descripcion

    \+ 1 o mas veces

    {n} se repite n veces

    {n,m} se repite dede n a m

    {n,} desde n hasta ...arriba

    \* (asterisco) 0 veces o mas
    \* ? 1 o ninguna /  perfecto para palabras plurales

    + → obligatorio (1 o más)
    ? → opcional pero solo una vez

    * → opcional y repetible (💥 el que necesitas aquí)

    Tambien se puede usar letras o simbolos especificos que necesiten estar
    como en un correo

### Ejemplo

```python

    def patron(correo):
        patron = r'\w+@\w+\. $'
        if re.search(patron,correo):
            print("Correo correcto")
```

> Aqui podemos ver un ejemplo donde el arroba forma parte general del correo, es decir no es parte de una secuencia mismai de caracteres, si no un mismo elemento puramente necesidado como tal.

#### Significado
>
>Corresponden a su nivel de aparicion, es decir, ?,* son para decir desde 0 hasta mas caracteres y ?, para solo una coincidencia de la palabra, es decir casa casa?
