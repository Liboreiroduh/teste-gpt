"""Funcoes utilitarias para calculos simples."""


def calcular_area(largura, comprimento):
    """Calcula a area de um retangulo."""
    return largura * comprimento


def calcular_valor(area, preco_m2):
    """Calcula o valor total com base na area e no preco por metro quadrado."""
    return area * preco_m2


def estimar_potencia(tensao, corrente):
    """Estima a potencia (P = V * I)."""
    return tensao * corrente


def estimar_corrente(potencia, tensao):
    """Estima a corrente (I = P / V)."""
    if tensao == 0:
        raise ValueError("Tensao nao pode ser zero")
    return potencia / tensao


def recomendar_processadora(area, potencia):
    """Retorna uma recomendacao simples de processadora.

    - industrial: potencia >= 2000 ou area >= 200
    - semi-industrial: potencia >= 1000 ou area >= 100
    - residencial: caso contrario
    """
    if potencia >= 2000 or area >= 200:
        return "industrial"
    if potencia >= 1000 or area >= 100:
        return "semi-industrial"
    return "residencial"
