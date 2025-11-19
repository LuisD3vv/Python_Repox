## Como funcionan

### Todas estas funciones realizan internamente un loop sobre cada elemento para aplicar la funcion por eso a veces no es necesario iterar de nuevo haciendo mas larga inecessariamente la funcion
>map()	Transforma cada elemento	Muchos (uno por elemento)
<pre>
def minutesToSeconds(lista):
    return lista[1] * 60

print("Minutos a segundos")
totalSeconds = list(map(minutesToSeconds,playlist))

</pre>
>filter()	Selecciona elementos según condición	Menos (solo los que cumplen)
<pre> def duracion(lista):
    return lista[1] > 5.00

print("Canciones de mayor duracion")
max_duracion = filter(duracion,playlist)
</pre>
>reduce() Combina todos en uno solo Uno, toma dos parametros internos la funcion, el aumento y el elementos siguiente asi como opcionalmente es el valor inicial del acomulador, 
<pre> 
def totalPlaytime(a,lista):
    numero = lista[1]
    return a + numero

print("La duraciones total de la playlist es de:")
totaltime = reduce(totalPlaytime,playlist,0)

</pre>

### Todas se pueden utilizar con lambda (funcion anonima)