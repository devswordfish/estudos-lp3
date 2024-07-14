def calcular_volume(comprimento: float, altura: float, largura: float) -> float:
    return (comprimento * altura * largura) / 1000

def calcular_potencia_termostato(volume: float, temperatura: float) -> float:
    return volume * 0.05 * (temperatura - 20)

def calcular_filtragem_minima(volume: float) -> tuple[float]:
    return (2 * volume, 3 * volume)
