
# Establecer o modificar el valor de un atributo, a menudo validando o transformando el dato antes de asignarlo.

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property # permite usar los atributos como si fueran publicos,
    def nombre(self):
        """Getter usando el decorador @property."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Setter usando el decorador @nombre.setter."""
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            print("Error: El nombre debe ser una cadena de texto no vacía.")

# Uso:
p = Persona("Ana")
print(p.nombre) # Llama al getter
p.nombre = "Ana María" # Llama al setter
