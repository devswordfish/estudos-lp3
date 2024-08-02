def calcular_imc(peso: float, altura: float) -> float:
    return peso / (altura * altura)

def classificacao_imc(imc: float) -> str:
    if imc < 18.5:
        return 'Baixo peso'

    if imc <= 24.9:
        return 'Peso normal'

    if imc <= 29.9:
        return 'Excesso de peso'

    if imc <= 34.9:
        return 'Obesidade de Classe 1'

    if imc <= 39.9:
        return 'Obesidade de Classe 2'

    return 'Obesidade de Classe 3'

def alcancar_peso_ideal(peso: float, altura: float, imc_alvo: float) -> float:
    altura_quadrada = altura * altura

    peso_alvo = imc_alvo * altura_quadrada

    peso_para_ganhar = peso_alvo - peso

    return peso_para_ganhar
