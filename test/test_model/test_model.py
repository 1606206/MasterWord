from src.model.model import *
from src.vista.vista import *
import tempfile
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
    # Mirar si no existe solo lleva a prints, no es necesario
    new_username = 'añadirPrueba'
    opciones = ['1','2']
    result = check_user(new_username, opciones[0],TEST_PATH,TEST_BBDD_NAME,1) # Llamar a la función con un usuario existente y opción 1
    # Verificar que se haya añadido un nuevo usuario
    df_result = pd.read_csv(TEST_PATH + '\\' + TEST_BBDD_NAME)
    assert result in df_result['USERNAMES'].values, "Falló la adición del nuevo usuario"

    df_result = df_result[df_result['USERNAMES'] != new_username]
    df_result.to_csv(TEST_PATH + '\\' + TEST_BBDD_NAME, index=False)


#-------------------------------- TEST SAVE USER DICT (EN PROCESO)---------------------------------------


def test_saveUserDict():
    username = "test1"
    result = saveUserDict(username, TEST_PATH, "test_user_dict", 1)
    assert result == 1  # Verificar que el resultado es 1 (guardado con éxito)

    # Verificar que el archivo fue creado
    assert os.path.isfile(os.path.join(TEST_PATH,"test_user_dict", 'dict_'+ username + '.csv'))
