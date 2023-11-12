from src.model.model import *
# UNIT TESTING

#------------------------TDD-----------------------#
def test_read_user():
    points, ranquing = read_user('serena', 1)
    assert points == 10
    assert ranquing == 1
    with pytest.raises(ValueError) as e:
        points, ranquing = read_user('noexisteix', 1)
    assert "L'usuari no s'ha trobat a la llista." in str(e.value)

    with pytest.raises(ValueError) as e:
        points, ranquing = read_user("", 1)
    assert "El nom no pot estar buit." in str(e.value)

'''

def test_saveUserDict(): #nomes es comprova que no estigui buit, hi ha una altra funcio on es comprova que ja existeixi
    guardat = 0
    guardat = saveUserDict("serena")
    assert guardat == 1

    with pytest.raises(ValueError) as e:
        guardat = saveUserDict("")
    assert "El nom no pot estar buit." in str(e.value)

## tambe sha dafegir a aquest test que el diccionari no estigui buit al guardar

''' #peta nse pq 


#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##

#------------------------TEST CAIXA BLANCA-----------------------#

##--------------------Statement Coverage-----------------------##
##---------------------Decision Coverage-----------------------##
##-----------------------Path Coverage-------------------------##
##-------------------Loop Testing Simple-----------------------##
##--------------------Loop Testing Aniuat----------------------##


'''def test_dictionary_checkLong_1():
    pass
    short_word = "short_word"
    long_word = "longlonglong_word"
    #assert not checkLong(short_word, long_word)

def test_dictionary_checkLong_2():
    pass

def test_dictionary_checkLong_3():
    pass


def test_dictionary_checkWord_1():
    pass

def test_dictionary_checkWord_2():
    pass

def test_dictionary_checkWord_3():
    pass
'''