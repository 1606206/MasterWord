import sys
sys.path.insert(1,'src/controlador')

from classWord import Word

'''TDD ANTIC
def test_toUppercase_1():
    word = Word("serena")
    word.toUpperCase()
    assert word.word == "SERENA"

def test_toUppercase_2():
    word = Word("MaStErWoRd")
    word.toUpperCase()
    assert word.word == "MASTERWORD"

def test_toUppercase_3():
    word = Word("PYTEST")
    word.toUpperCase()
    assert word.word == "PYTEST"

def test_splitWord_1():
    word = Word("serena")
    word.toSplitWord()
    assert word.splitted_word == ['s','e','r','e','n','a']
    
def test_splitWord_2():
    word = Word("UAB")
    word.toSplitWord()
    assert word.splitted_word == ['U','A','B']

def test_splitWord_3():
    word = Word("qwerty12345")
    word.toSplitWord()
    assert word.splitted_word == ['q','w','e','r','t','y','1','2','3','4','5']
    '''

# INICIALIZACION DE UNA PALABRA
def test_init_1():
    word = Word("palabra")
    assert word.palabra == "palabra"
    assert word.n_letters == 7
    assert word.splitWord == ['P', 'A', 'L', 'A', 'B', 'R', 'A']
    
# PALABRA CON NUMEROS
def test_validInput_1():
    word = Word("hola1234")
    assert isinstance(word.palabra, str)  #  COMPROBANDO QUE EL INPUT ES UN STRING
    assert word.palabra.isalpha()  #  COMPROBANDO QUE SÓLO HAY LETRAS
    assert word.n_letters > 0  # COMPROBANDO QUE LA PALABRA NO ESTÁ VACÍA
    
# PALABRA CON ESPACIOS
def test_validInput_2():
    word = Word("H O L A")
    assert isinstance(word.palabra, str)  #  COMPROBANDO QUE EL INPUT ES UN STRING
    assert word.palabra.isalpha()  #  COMPROBANDO QUE SÓLO HAY LETRAS
    assert word.n_letters > 0  # COMPROBANDO QUE LA PALABRA NO ESTÁ VACÍA

# PALABRA CON CARACTERES ESPECIALES
def test_validInput_3():
    word = Word("SERENA+-*/")
    assert isinstance(word.palabra, str)  #  COMPROBANDO QUE EL INPUT ES UN STRING
    assert word.palabra.isalpha()  #  COMPROBANDO QUE SÓLO HAY LETRAS
    assert word.n_letters > 0  # COMPROBANDO QUE LA PALABRA NO ESTÁ VACÍA
    
# PALABRA VACÍA
def test_validInput_4():
    word = Word("")
    assert isinstance(word.palabra, str)  #  COMPROBANDO QUE EL INPUT ES UN STRING
    assert word.palabra.isalpha()  #  COMPROBANDO QUE SÓLO HAY LETRAS
    assert word.n_letters > 0  # COMPROBANDO QUE LA PALABRA NO ESTÁ VACÍA

# PALABRA QUE NO ES STRING
def test_validInput_5():
    word = Word(999)
    assert isinstance(word.palabra, str)  #  COMPROBANDO QUE EL INPUT ES UN STRING
    assert word.palabra.isalpha()  #  COMPROBANDO QUE SÓLO HAY LETRAS --> esto va a petar siempre con este test pq no se pude cambiar, dejo debajo una posible modificacion
    assert word.n_letters > 0  # COMPROBANDO QUE LA PALABRA NO ESTÁ VACÍA

# PALABRA QUE NO ES STRING
def test_validInput_6():
    word = Word(999)
    assert word.palabra == "999"
    assert word.n_letters == 3
    assert word.splitWord == None


#------------------------TEST CAIXA NEGRA-----------------------#

##------------------Particions equivalents---------------------##

##------------------Valors límit i frontera--------------------##
