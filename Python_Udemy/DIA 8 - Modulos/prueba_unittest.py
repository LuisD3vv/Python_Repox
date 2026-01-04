"""Importar modulo unitestt"""
import unittest
import ejemplo_unittest

"""
unittest es un metodo o una herramienta
nos ayuda para determinar si un modulo o un conjunto 
de modulos de codigo funciona correctamente.

"""

class probar_cambiaTexto(unittest.TestCase):
    """
    Este es una clase para comprobar el resultado que da el modulo
    en comparacion con el que esperamos tener
    
    Basicamente hace una comparacion para comprobar si el modulo que creamos hace lo deseado comparandolo
    con un resultado o varible ya predefinida que contiene el valor final que deseamos
    """
    
    # Una buena practica es nombrar las funciones iniciando con test
    def test_mayusculas(self):
        palabra = 'Buen dia'
        resultado = ejemplo_unittest.todo_mayusculas(palabra)# modulo-funcion-parametro
        self.assertEqual(resultado, 'BUEN DIA') # prueba que nos permite evaluar si el resultado es igual al que esperamos que sea,


# es una condicion especial que se usa para controlar que el que se esta ejecutando directamente es el mismo archivo que tiene los test
# o si esta siendo importado como modulo por otro archivo
if __name__ == '__main__':
    unittest.main()
else:
    print("not the main file")

"""
Si el archivo principal es el que tiene la funcion que se quiere comprobar
entonces se ejecutara este test, ya que main el nombre, pasara a ser el main.
"""
