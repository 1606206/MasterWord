
class MockInput():
    def __init__(self, llista_paraules):
        self.llista_paraules = llista_paraules
        self.cont = 0
    
    def get_word(self):
        paraula = self.llista_paraules[self.cont]
        self.cont += 1
        return paraula
