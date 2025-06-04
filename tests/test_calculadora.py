import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest

from calculadora import (
    calcular_area,
    calcular_valor,
    estimar_potencia,
    estimar_corrente,
    recomendar_processadora,
)


def test_calcular_area():
    assert calcular_area(3, 4) == 12
    assert calcular_area(0, 10) == 0


def test_calcular_valor():
    area = calcular_area(5, 2)
    assert calcular_valor(area, 10) == 100


def test_estimar_potencia():
    assert estimar_potencia(220, 5) == 1100


def test_estimar_corrente():
    assert estimar_corrente(1100, 220) == 5
    with pytest.raises(ValueError):
        estimar_corrente(100, 0)


def test_recomendar_processadora():
    assert recomendar_processadora(50, 500) == "residencial"
    assert recomendar_processadora(150, 1500) == "semi-industrial"
    assert recomendar_processadora(250, 2500) == "industrial"
