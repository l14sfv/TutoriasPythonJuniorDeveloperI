#Ejercicio 1 - plataforma de musica
#Artista
class Artista:
    def __init__(self, nombre_artistico, genero_musical, pais, verificada, seguidores):
        self.nombre_artistico = nombre_artistico
        self.genero_musical = genero_musical
        self.pais = pais
        self.verificada = verificada
        self.__seguidores = 0
        self.set_seguidores(seguidores)
        
    def get_seguidores(self):
        return self.__seguidores
    def set_seguidores(self, seguidores):
        if seguidores >= 0:
            self.__seguidores = seguidores
        else:
            print("El número de seguidores no puede ser negativo.")

class Cancion:
    def __init__(self, titulo, artista, duracion, reproducciones):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
        self.reproducciones = reproducciones

#class main
from artista import Artista
from cancion import Cancion

artista1 = Artista("Shakira", "Pop", "Colombia", True, 50000000)
cancion1 = Cancion("Loba", artista1, "3:05", 10000000)

print("Titulo de la canción:", cancion1.titulo)
print("Nombre del Artista:", cancion1.artista.nombre_artistico)
print("Pais del artista:", cancion1.artista.pais)
print("Seguidores del artista:", cancion1.artista.get_seguidores())

artista1.set_seguidores(60000000)
print("Seguidores del artista después de actualización:", artista1.get_seguidores())

artista1.set_seguidores(-100)  # Intento de establecer seguidores negativos
print("Seguidores del artista después de intento de actualización negativa:", artista1.get_seguidores())
#Main

#Ejercicio 2 - plataforma de streaming de video

#Ejercicio 3
