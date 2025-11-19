# def cambiar_letras(tipo):
    
#     def mayusculas(texto):
#         print(texto.upper())
    
    
#     def minusculas(texto):
#         print(texto.lower())
    
#     if tipo == "may":
#         return mayusculas
#     elif tipo == "min":
#         return minusculas

# operacion = cambiar_letras('may')
# operacion("luis")

def decorar_saludo(funcion): 
    
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion


@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

@decorar_saludo
def minusculas(texto):
    print(texto.lower())


mayuscula_decorada = (decorar_saludo(mayusculas))
mayuscula_decorada('luis')

#Pyqt6
