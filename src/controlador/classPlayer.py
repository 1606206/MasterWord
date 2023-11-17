from src.model.model import *
from src.model.classDictionary import *

class Player:
    """Clase para representar a un jugador"""
    def __init__(self, name="anonymous", points=0, ranking=0):
        self.set_name(name)
        self.set_points(points)
        self.set_ranking(ranking)

    def get_name(self):
        """Getter para el atributo name"""
        return self.name

    def set_name(self, name):
        """Setter para el atributo name"""
        if not isinstance(name, str):
            raise TypeError("Has d'introduir un string.")
        if len(name) <= 0:
            raise ValueError("El nom no pot estar buit.")
        self.name = name

    def get_points(self):
        """Getter para el atributo points"""
        return self.points

    def set_points(self, points):
        """Setter para el atributo points"""
        if not isinstance(points, int):
            raise TypeError("La puntuació només pot ser un enter.")
        if points < 0:
            raise ValueError("La puntuació no pot ser negativa.")
        self.points = points

    def get_ranking(self):
        """Getter para el atributo ranking"""
        return self.ranking

    def set_ranking(self, ranking):
        """Setter para el atributo ranking"""
        if not isinstance(ranking, int):
            raise TypeError("El ranking només pot ser un enter.")
        if ranking < 0:
            raise ValueError("El ranking no pot ser negatiu.")
        self.ranking = ranking


