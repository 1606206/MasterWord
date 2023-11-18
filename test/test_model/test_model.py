from src.model.model import *
from src.vista.vista import *
import pandas as pd
from io import StringIO
import os
# UNIT TESTING
PATH = 'test_BBDD'
FUNCIONES_POR_TESTEAR_PARA_STATEMENT_COVERAGE = "ESTOY UTILIZANDO UNA BASE DE DATOS DE TEST, PERO LAS FUNCIONES DEL MODEL ACCEDEN A LA BASE DE DATOS REAL, POR TANTO FALLA"
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
#--------------------------------TEST SAVE USER POINTS---------------------------------------
#FALLA CONTROLADOR_CANVIS_GUARDATS_CORRECTAMENT
def test_save_user_points(capfd):
    save_user_points('user2', 15)# Llamar a la función con nuevos puntos
    out, _ = capfd.readouterr() # Capturar la salida estándar
    assert "sumant  15 punts al usuari  user2" in out, "Falló la impresión de la operación"# Verificar la salida
    df_result = pd.read_csv(PATH + '\\test_user_names.csv')# Verificar que los puntos se han actualizado correctamente
    assert df_result.loc[df_result['USERNAMES'] == 'user2', 'POINTS'].values[0] == 35, "Falló la actualización de puntos"

#------------------------------------TEST CHECK USER-----------------------------------------------
#FALLA CONTROLADOR_NOM_JA_EXISTENT
def test_check_user(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1') # Mockear la entrada del usuario para simular la opción 1
    result = check_user('user2', '1') # Llamar a la función con un usuario existente y opción 1
    out, _ = capfd.readouterr() # Capturar la salida estándar
    assert "Benvingut" in out, "Falló el mensaje de bienvenida" # Verificar que el mensaje de bienvenida se imprima
    assert result != 'user2', "Falló la actualización del nombre de usuario"  # Verificar que el resultado sea el nuevo nombre de usuario
    # Verificar que se haya añadido un nuevo usuario
    df_result = pd.read_csv(PATH + '\\test_user_names.csv')
    assert result in df_result['USERNAMES'].values, "Falló la adición del nuevo usuario"

    
    monkeypatch.setattr('builtins.input', lambda _: '2') # Mockear la entrada del usuario para simular la opción 2
    result = check_user('user1', '2')  # Llamar a la función con un usuario existente y opción 2
    out, _ = capfd.readouterr() # Capturar la salida estándar
    assert "Benvingut" in out, "Falló el mensaje de bienvenida" # Verificar que el mensaje de bienvenida se imprima
    assert result == 'user1', "Falló el mantenimiento del nombre de usuario existente" # Verificar que el resultado sea el mismo nombre de usuario




#-------------------------------- TEST SAVE USER DICT (EN PROCESO)---------------------------------------
def test_saveUserDict(tmp_path):
    # Establecer el directorio temporal para la prueba
    tmp_path = tmp_path / "test_BBDD" / "test_user_dict"
    tmp_path.mkdir(parents=True)

    # Mockear la función controlador_directrius_nou_diccionari()
    def mock_controlador_directrius_nou_diccionari():
        return "word1 word2 word3"

    # Mockear la función controlador_canvis_guardats_correctament()
    def mock_controlador_canvis_guardats_correctament():
        pass

    # Llamar a la función con un nombre de usuario válido
    with pytest.raises(ValueError, match="El nom no pot estar buit."):
        test_username = ""
        saveUserDict(test_username)

    # Llamar a la función con un nombre de usuario válido
    test_username = "user1"
    with pytest.raises(FileNotFoundError):
        saveUserDict(test_username)

    # Llamar a la función con un nombre de usuario válido
    test_username = "user2"
    with pytest.raises(FileNotFoundError):
        saveUserDict(test_username)

    # Llamar a la función con un nombre de usuario válido
    test_username = "user3"
    with pytest.raises(FileNotFoundError):
        saveUserDict(test_username)

    # Llamar a la función con un nombre de usuario válido
    test_username = "serena"
    with pytest.raises(FileNotFoundError):
        saveUserDict(test_username)

    # Llamar a la función con un nombre de usuario válido
    test_username = "test_user"
    saveUserDict(test_username)

    # Verificar que se haya creado el archivo correctamente
    file_path = tmp_path / "test_user_dict.csv"
    assert file_path.is_file(), "Falló la creación del archivo"
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