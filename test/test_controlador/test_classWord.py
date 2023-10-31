import sys
sys.path.insert(1,'src/controlador')

from classWord import Word

    
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
