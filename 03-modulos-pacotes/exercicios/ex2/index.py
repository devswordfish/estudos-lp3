'''
Ex02. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), crie uma calculadora que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

IMC = peso / altura * altura

Classificação
----------------------------------
IMC           Classificação
-----------------------------------
< 18,5             Baixo peso
18,5 a 24,9     Peso normal
25,0 a 29,9     Excesso de peso
30,0 a 34,9     Obesidade de Classe 1
35,0 a 39,9     Obesidade de Classe 2
>= 40,00         Obesidade de Classe 3
'''

from imc import calcular_imc, classificacao_imc, alcancar_peso_ideal


def float_input(prompt: str) -> float:
    while True:
        try:
            number = float(input(prompt))
            break
        except ValueError:
            print('Digite um número válido!')
    return number


peso = float_input('Digite o seu peso (Kg): ')
altura = float_input('Digite a sua altura (m): ')

imc = calcular_imc(peso, altura)
classificacao = classificacao_imc(imc)
peso_para_ganhar = alcancar_peso_ideal(peso, altura, 24.9)

ganhar_ou_perder = 'ganhar' if peso_para_ganhar >= 0 else 'perder'

print('-' * 20 + 'IMC' + '-' * 20)
print(f'Seu IMC é {imc}')
print(f'Você está na faixa "{classificacao}"')
print(f'Para atingir o IMC de 24,9 você deve {ganhar_ou_perder} {abs(peso_para_ganhar)}Kg')
