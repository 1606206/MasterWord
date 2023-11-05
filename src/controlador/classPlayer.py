import sys
sys.path.insert(2,'src/model')
from model import *

## clase Jugador
class Player: 
    def __init__(self, name="anonymous", points=0, ranking=0):
        if not isinstance(name, str):
            raise TypeError("Has d'introduir un string.")
        if len(name) <= 0:
            raise ValueError("El nom no pot estar buit.")
        if not isinstance(points, int):
            raise TypeError("La puntuació només pot ser un enter.")
        if points < 0:
            raise ValueError("La puntuació no pot ser negativa.")
        if not isinstance(ranking, int):
            raise TypeError("El ranking només pot ser un enter.")
        if ranking < 0:
            raise ValueError("El ranking no pot ser negatiu.")
        self.name = name
        self.points = points
        self.ranking = ranking

    # Getter para el atributo 'name'
    def get_name(self):
        return self.name

    # Setter para el atributo 'name'
    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Has d'introduir un string.")
        if len(name) <= 0:
            raise ValueError("El nom no pot estar buit.")
        self.name = name

    # Getter para el atributo 'points'
    def get_points(self):
        return self.points

    # Setter para el atributo 'points'
    def set_points(self, points):
        if not (isinstance(points, int) or isinstance(points, float)):
            raise TypeError("La puntuació no és un número.")
        self.points = points

    # Getter para el atributo 'ranking'
    def get_ranking(self):
        return self.ranking

    # Setter para el atributo 'ranking'
    def set_ranking(self, ranking):
        if not isinstance(ranking, int):
            raise TypeError("El ranking només pot ser un enter.")
        self._ranking = ranking


