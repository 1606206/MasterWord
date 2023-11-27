from src.model.model import *
from src.vista.vista import *
from unittest.mock import patch
import pandas as pd
import os
import shutil
import tempfile

# UNIT TESTING
TEST_PATH = 'test_BBDD'
TEST_BBDD_NAME = "test_user_names.csv"

#TEST READ USER
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

#TEST SAVE USER POINTS
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

#TEST CHECK USER
def test_check_user():
    #guardamos el df que no queremos que se modifique 
    df_original = pd.read_csv(TEST_PATH + '\\' + TEST_BBDD_NAME, sep=',')
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
    df_original.to_csv(TEST_PATH + '\\' + TEST_BBDD_NAME, index=False, sep=',')

#DECISION COVERAGE FUNCIÓN CHECKUSER
def test_check_user_decision_coverage_1():
    # Cargar el DataFrame original desde el archivo CSV
    df_original = pd.read_csv('BBDD' + '\\' + 'user_names.csv', sep=',')
    # Simular la entrada del usuario como 'nuevo_nombre_de_usuario'
    with patch('builtins.input', return_value='nuevo_nombre_de_usuario'):
        # Ejecutar la función check_user con 'serena', '1' y test=1
        username = check_user('serena', '1', test=1)
    # Verificar que la función haya devuelto 'nuevo_nombre_de_usuario'
    assert username == 'nuevo_nombre_de_usuario'
    # Restaurar el DataFrame original después de la prueba
    df_original.to_csv('BBDD' + '\\' + 'user_names.csv', index=False, sep=',')


def test_check_user_decision_coverage_2():
    df_original = pd.read_csv(TEST_PATH + '\\' + TEST_BBDD_NAME, sep=',')
    missing_username = 'no_existo_bb'
    with patch("pandas.read_csv") as mock_read_csv:
        # Configura el comportamiento del objeto simulado para que el usuario exista después de la opción 1
        mock_read_csv.side_effect = [pd.DataFrame({'USERNAMES': [missing_username]}), pd.DataFrame({'USERNAMES': [missing_username]})]
        # Llama a la función check_user con el mismo usuario y opción 2.
        try:
            result_missing_user_option_2 = check_user(missing_username, '2', TEST_PATH, TEST_BBDD_NAME, 1)
            # Si no hay excepciones, la función se ejecutó con éxito.
            # Verifica que el resultado de la función sea el mismo que el nombre de usuario proporcionado
            assert result_missing_user_option_2 == missing_username, f"El resultado no coincide con el nombre de usuario proporcionado: {result_missing_user_option_2}"
        except Exception as e:
            pytest.fail(f"Error inesperado: {e}")
    df_original.to_csv(TEST_PATH + '\\' + TEST_BBDD_NAME, index=False, sep=',')




#TEST SAVE USER DICT
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
