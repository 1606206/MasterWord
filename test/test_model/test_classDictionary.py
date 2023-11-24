from src.model.classDictionary import *

def test_init_1():
    # Prueba la inicialización de la clase Dictionary con valores predeterminados.
    dictionary = Dictionary()  
    assert dictionary.default == 1  
    assert dictionary.level == 1 
    assert dictionary.path == None  

def test_init_2():
    # Prueba la inicialización de la clase Dictionary con valores diferentes a los predeterminados.
    dictionary = Dictionary(default=0, level=2, secPath='\dictionary_3.csv')
    assert dictionary.default == 0
    assert dictionary.level == 2
    assert dictionary.path == '\dictionary_3.csv'

# Comprueba que randomChoice devuelve un elemento dentro de wordList.
def test_randomChoice():
    dictionary = Dictionary(0, 1, '\dictionary_3.csv')
    assert dictionary.randomChoice() in dictionary.wordList



