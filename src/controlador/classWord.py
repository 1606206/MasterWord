def transformWord(palabra): ## donde ponemos esta funciónn???
    splitWord = []
    palabra = palabra.upper()
   # print("palabra en mayusculas", palabra)
    for i in palabra:
        splitWord.append(i)
    #print("palabra split", splitWord)
    return splitWord

class Word:
    #guardamos la letra
    def __init__(self, palabra):
        self.palabra = palabra
        self.n_letters = len(palabra)
        self.splitWord = transformWord(palabra)
        #comprobar espacios
        #comprobar numeros en el string
        #comporbar entrada de enteros o flotantes
    '''
    #dada la palabra seleccionada la divide y devuelve un array separado listo para jugar
    def split_word(self):
        for i in self.word:
            self.splitWord.append(i)
        print("palabra split", self.splitWord)

    #convierte las letras de la palabra a mayusculas
    def toUppercase(self):
        self.word = self.word.upper()
        print("palabra en mayusculas", self.word)
        '''



