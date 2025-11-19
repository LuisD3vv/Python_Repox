def saludar_persona(nombre):
    print("Hola " + nombre)
    """
    Esta funcion sirve para saludar a las personas
    colocando definiendo la funcion saludar_persona
    luegpo se le coloque el parametro nombre, el cual al llamar
    a la funcion posteriorimente, junto con un nombre imprimira
    el hola + el nombre otorgado
    """
saludar_persona("Luis")

# Las funciones pueden usarse de diferentes formas, ya sea como simple funcion, en un if, o incluso en una variable


resultado = saludar_persona("eduardo")

if saludar_persona("luis") == 'Hola Luis':
    print(True)
    