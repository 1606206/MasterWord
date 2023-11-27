from src.controlador.controlador import *
from pytest_mock import mocker


def test_continuar_o_tancarjoc(mocker):
    mocker.patch("builtins.input", return_value='C')
    respuesta = continuar_o_tancarjoc()
    assert respuesta == True

    mocker.patch("builtins.input", return_value='X')
    respuesta = continuar_o_tancarjoc()
    assert respuesta == False
    
