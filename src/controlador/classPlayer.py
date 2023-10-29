import sys
sys.path.insert(2,'src/model')
from model import *

## clase Jugador
class Player: 
    def __init__(self, name="anonymous"):
        self.name = name
        if name != "anonymous":
            self.points, self.ranking = read_user(name)
        else:
            self.points, self.ranking = 0,0

    # Getter para el atributo 'name'
    def get_name(self):
        return self.name

    # Setter para el atributo 'name'
    def set_name(self, name):
        self.name = name

    # Getter para el atributo 'points'
    def get_points(self):
        return self.points

    # Setter para el atributo 'points'
    def set_points(self, points):
        self.points = points

    # Getter para el atributo 'ranking'
    def get_ranking(self):
        return self.ranking

    # Setter para el atributo 'ranking'
    def set_ranking(self, ranking):
        self._ranking = ranking


