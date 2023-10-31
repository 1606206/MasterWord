class Word:
    def __init__(self, palabra):
        if not isinstance(palabra, str):
            raise TypeError("Has d'introduir un string")
        if not palabra.isalpha():
            raise ValueError("La paraula només pot contenir lletres")
        if len(palabra) <= 0:
            raise ValueError("La paraula no pot estar buida")

        self.palabra = str(palabra.upper())
        self.n_letters = len(self.palabra)
        self.splitWord = self.palabra.split()
