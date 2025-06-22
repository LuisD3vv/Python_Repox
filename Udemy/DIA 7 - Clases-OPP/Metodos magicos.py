# mi_lista = [1,1,1,1,1,1,1]
# print(mi_lista)


# class Objeto:
#     ...


# mi_objeto = Objeto()
# print(mi_objeto)

class CD:

    def __init__(self, autor, titulo,canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    #metodo str, definir como se veran los metodos al ser solicitados
    def __str__(self):
        return f"Album: '{self.titulo}' de {self.autor}"
    def __len__(self):
        return self.canciones
    def __del__(self):
        print("Se ha elmindado correctamente {}".format(self)) # Muestra el libro
    #Cuenta con muchos mas

mi_cd = CD('Queen', 'The game', 15)

print(mi_cd)
print(len(mi_cd))


#Eliminar instancia
del mi_cd