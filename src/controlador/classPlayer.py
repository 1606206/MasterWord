## clase Jugador
class Player: 
    def __init__(self, name="anonymous", points=0, ranking=0):
        self._name = name
        self._points = points
        self._ranking = ranking

    # Getter para el atributo 'name'
    def get_name(self):
        return self._name

    # Setter para el atributo 'name'
    def set_name(self, name):
        self._name = name

    # Getter para el atributo 'points'
    def get_points(self):
        return self._points

    # Setter para el atributo 'points'
    def set_points(self, points):
        self._points = points

    # Getter para el atributo 'ranking'
    def get_ranking(self):
        return self._ranking

    # Setter para el atributo 'ranking'
    def set_ranking(self, ranking):
        self._ranking = ranking

