import sys
sys.path.insert(1,'src/controlador')

from classDictionary import Dictionary

def test_init_1(): #clase vacía, para comprobar los valores por defecto
    dictionary = Dictionary()  
    assert dictionary.default == 1  
    assert dictionary.level == 1 
    assert dictionary.path == None  

def test_init_2(): #posem valors diferents als de per defecte
    dictionary = Dictionary(default=0,level=2,secPath='ruta.csv')
    assert dictionary.default == 0
    assert dictionary.level == 2
    assert dictionary.path == 'ruta.csv' #no entiendo pq me peta
    #como hago lo del wordlist??

#read BBDD se tiene que hacer con un mock object??

# comprovem que randomChoice retorna un element dins de wordList
def test_randomChoice():
    dictionary = Dictionary(0, 1, '\dictionary_3.csv')
    assert dictionary.randomChoice() in dictionary.wordList

#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##

