'''
Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e calcule as seguintes informações.
- O volume do aquário em litros;
- A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
- A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

- Volume é dado por (comprimento * altura * largura) / 1000
- A potência do termostato depende do tamanho do aquário e da temperatura ambiente. Para o cálculo utilizar a fórmula: potencia
- volume * 0,05 * (temperatura desejada - temperatura ambiente)
- A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.
'''

from aquario import calcular_volume, calcular_potencia_termostato ,calcular_filtragem_minima


def float_input(prompt: str) -> float:
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print('Digite um número válido!')
    return number


comprimento = float_input('Digite o comprimento do aquário em cm: ')
largura = float_input('Digite a largura do aquário em cm: ')
altura = float_input('Digite a altura do aquário em cm: ')
temperatura = float_input('Digite a temperatura desejada do aquário em °C: ')

volume = calcular_volume(comprimento, altura, largura)
potencia_termostato = calcular_potencia_termostato(volume, temperatura)
filtragem_2min, filtragem_3min = calcular_filtragem_minima(volume)

print('-' * 20 + 'INFORMAÇÕES IMPORTANTES' + '-' * 20)
print(f'Para um aquário de medidas {comprimento} x {largura} x {altura} com temperatura {temperatura}°C temos:')
print(f'- Volume: {volume}L')
print(f'- Potência do termostato: {potencia_termostato}W')
print(f'- Filtragem por hora: {filtragem_2min}L ou {filtragem_3min}L por hora')
