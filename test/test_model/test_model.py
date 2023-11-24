from src.model.model import *
from src.vista.vista import *
import pandas as pd
import os

# UNIT TESTING
TEST_PATH = 'test_BBDD'
TEST_BBDD_NAME = "test_user_names.csv"

#------------------------TEST READ USER-----------------------#
def test_read_user():
    # Prueba la función read_user con casos específicos.
    # Caso de usuario existente ('serena') con puntos conocidos (1000).
    points, ranquing = read_user('serena', 1000, TEST_PATH, TEST_BBDD_NAME)
    assert points == 1000
    assert ranquing == 1
    
    # Caso de usuario inexistente ('noexisteix').
    # Se espera que se genere un ValueError con el mensaje indicando que el usuario no se encuentra en la lista.
    with pytest.raises(ValueError) as e:
        points, ranquing = read_user('noexisteix', 1, TEST_PATH, TEST_BBDD_NAME)
    assert "L'usuari no s'ha trobat a la llista." in str(e.value)

    # Caso de nombre de usuario vacío.
    # Se espera que se genere un ValueError con el mensaje indicando que el nombre no puede estar vacío.
    with pytest.raises(ValueError) as e:
        points, ranquing = read_user("", 1, TEST_PATH, TEST_BBDD_NAME)
    assert "El nom no pot estar buit." in str(e.value)

#--------------------------------TEST SAVE USER POINTS---------------------------------------
def test_save_user_points():
    # Lee los puntos anteriores del usuario 'almendruco'.
    df_result_anterior = pd.read_csv(TEST_PATH + '\\test_user_names.csv')
    punts_anteriors = df_result_anterior.loc[df_result_anterior['USERNAMES'] == 'almendruco', 'POINTS'].values[0]
    # Llama a la función save_user_points con un nuevo puntaje de 1.
    save_user_points('almendruco', 1, TEST_PATH, TEST_BBDD_NAME, 1)
    # Lee los puntos actualizados del usuario 'almendruco'.
    df_result = pd.read_csv(TEST_PATH + '\\test_user_names.csv')
    # Verifica que los puntos se han actualizado correctamente.
    assert df_result.loc[df_result['USERNAMES'] == 'almendruco', 'POINTS'].values[0] == (punts_anteriors + 1), "Falló la actualización de puntos"




#------------------------------------TEST CHECK USER-----------------------------------------------
def test_check_user():
    # Nuevo nombre de usuario para la prueba.
    new_username = 'añadirPrueba'
    # Opciones posibles: ['1', '2']
    opciones = ['1', '2']
    # Llama a la función check_user con un nuevo usuario existente y opción 1.
    result = check_user(new_username, opciones[0], TEST_PATH, TEST_BBDD_NAME, 1)
    # Verifica que se haya añadido el nuevo usuario al archivo CSV.
    df_result = pd.read_csv(TEST_PATH + '\\' + TEST_BBDD_NAME)
    assert result in df_result['USERNAMES'].values, "Falló la adición del nuevo usuario"
    # Elimina el usuario de la base de datos para dejarla en su estado original.
    df_result = df_result[df_result['USERNAMES'] != new_username]
    df_result.to_csv(TEST_PATH + '\\' + TEST_BBDD_NAME, index=False)



#-------------------------------- TEST SAVE USER DICT---------------------------------------
def test_saveUserDict():
    # Nombre de usuario para la prueba.
    username = "test1"
    # Llama a la función saveUserDict con un nombre de usuario existente y una carpeta de prueba.
    result = saveUserDict(username, TEST_PATH, "test_user_dict", 1)
    # Verifica que el resultado es 1 (guardado con éxito).
    assert result == 1
    # Verifica que el archivo fue creado.
    assert os.path.isfile(os.path.join(TEST_PATH, "test_user_dict", 'dict_'+ username + '.csv'))
    # Prueba con un nombre de usuario vacío.
    username_empty = ""
    # Se espera que se genere un ValueError con el mensaje indicando que el nombre no puede estar vacío.
    with pytest.raises(ValueError, match="El nom no pot estar buit."):
        saveUserDict(username_empty, TEST_PATH, "test_user_dict", 1)
