from src.model.model import *
from src.vista.vista import *
import pandas as pd
from io import StringIO
import os
# UNIT TESTING
TEST_PATH = 'test_BBDD'
TEST_BBDD_NAME = "test_user_names.csv"
FUNCIONES_POR_TESTEAR_PARA_STATEMENT_COVERAGE = "ESTOY UTILIZANDO UNA BASE DE DATOS DE TEST, PERO LAS FUNCIONES DEL MODEL ACCEDEN A LA BASE DE DATOS REAL, POR TANTO FALLA"
#------------------------TDD-----------------------#

#FUNCIONA
def test_read_user():
    points, ranquing = read_user('serena', 1,TEST_PATH,TEST_BBDD_NAME)
    assert points == 1000
    assert ranquing == 1
    with pytest.raises(ValueError) as e:
        points, ranquing = read_user('noexisteix', 1,TEST_PATH,TEST_BBDD_NAME)
    assert "L'usuari no s'ha trobat a la llista." in str(e.value)

    with pytest.raises(ValueError) as e:
        points, ranquing = read_user("", 1,TEST_PATH,TEST_BBDD_NAME)
    assert "El nom no pot estar buit." in str(e.value)

#--------------------------------TEST SAVE USER POINTS---------------------------------------
#FUNCIONA
def test_save_user_points():
    df_result_anterior = pd.read_csv(TEST_PATH + '\\test_user_names.csv')# Verificar que los puntos se han actualizado correctamente
    punts_anteriors =  df_result_anterior.loc[df_result_anterior['USERNAMES'] == 'almendruco', 'POINTS'].values[0]
    save_user_points('almendruco', 1,TEST_PATH,TEST_BBDD_NAME,1)# Llamar a la función con nuevos puntos
    df_result = pd.read_csv(TEST_PATH + '\\test_user_names.csv')# Verificar que los puntos se han actualizado correctamente
    assert df_result.loc[df_result['USERNAMES'] == 'almendruco', 'POINTS'].values[0] == (punts_anteriors+1), "Falló la actualización de puntos"



#------------------------------------TEST CHECK USER-----------------------------------------------
#FALLA CONTROLADOR_NOM_JA_EXISTENT
def test_check_user(capfd):
    #---------------------USUARIO EXISTENTE------------------------------------
    new_username = 'añadirPrueba'
    opciones = ['1','2']
    result = check_user(new_username, opciones[0],TEST_PATH,TEST_BBDD_NAME,1) # Llamar a la función con un usuario existente y opción 1
    #out, _ = capfd.readouterr() # Capturar la salida estándar
    #assert "Aquest nom d'usuari ja existeix. Introdueix un altre nom de usuari: " in out, "Falló el mensaje de bienvenida" # Verificar que el mensaje de bienvenida se imprima
    #assert result != 'serena', "Falló la actualización del nombre de usuario"  # Verificar que el resultado sea el nuevo nombre de usuario
    # Verificar que se haya añadido un nuevo usuario
    df_result = pd.read_csv(TEST_PATH + '\\' + TEST_BBDD_NAME)
    assert result in df_result['USERNAMES'].values, "Falló la adición del nuevo usuario"

    df_result = df_result[df_result['USERNAMES'] != new_username]
    df_result.to_csv(TEST_PATH + '\\' + TEST_BBDD_NAME, index=False)

'''
    
    monkeypatch.setattr('builtins.input', lambda _: '2') # Mockear la entrada del usuario para simular la opción 2
    result = check_user('serena', '2',TEST_PATH,TEST_BBDD_NAME)  # Llamar a la función con un usuario existente y opción 2
    out, _ = capfd.readouterr() # Capturar la salida estándar
    assert "Benvingut" in out, "Falló el mensaje de bienvenida" # Verificar que el mensaje de bienvenida se imprima
    assert result == 'serena', "Falló el mantenimiento del nombre de usuario existente" # Verificar que el resultado sea el mismo nombre de usuario

    #---------------------USUARIO NO EXISTENTE------------------------------------


    monkeypatch.setattr('builtins.input', lambda _: '1') 
    result = check_user('noexisteix', '1', TEST_PATH, TEST_BBDD_NAME)
    out, _ = capfd.readouterr()
    assert "Benvingut" in out, "Falló el mensaje de bienvenida"
    assert result != 'noexisteix', "Falló la actualización del nombre de usuario"
    df_result = pd.read_csv(TEST_PATH + '\\' + TEST_BBDD_NAME)
    assert result in df_result['USERNAMES'].values, "Falló la adición del nuevo usuario"

    # Opción 2: Intentar entrar con el nombre de usuario no existente
    monkeypatch.setattr('builtins.input', lambda _: '2') 
    result = check_user('noexisteix', '2', TEST_PATH, TEST_BBDD_NAME)
    out, _ = capfd.readouterr()
    assert "Benvingut" not in out, "Falló el mensaje de bienvenida"
    assert result == 'noexisteix', "Falló el mantenimiento del nombre de usuario no existente"



'''
'''
#-------------------------------- TEST SAVE USER DICT (EN PROCESO)---------------------------------------
def mock_controlador_directrius_nou_diccionari():
    return "word1 word2 word3"

def test_saveUserDict(capfd, monkeypatch):
    monkeypatch.setattr(controlador_directrius_nou_diccionari, mock_controlador_directrius_nou_diccionari)

    # Caso de prueba exitoso
    result = saveUserDict('serena',TEST_PATH, "test_user_dict")
    out, _ = capfd.readouterr()
    assert "Canvis guardats correctament." in out
    assert result == 1

    # Caso de prueba con nombre de usuario vacío
    with pytest.raises(ValueError, match="El nom no pot estar buit."):
        saveUserDict('')

    # Verificar que se haya creado el archivo correctamente
    with open('test_BBDD\\test_user_dict\\serena.csv', 'r') as checkFile:
        content = checkFile.read()
        assert "Palabras\nword1\nword2\nword3" in content
'''




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