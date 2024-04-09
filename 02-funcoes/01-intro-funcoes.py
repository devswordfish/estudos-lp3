# Função

# Declaração
# def nome_da_funcao(parametro1, parametro2):
#   return valor

# Função sem retorno e sem parâmetro
def imprimir_saudacao():
    print('Bom dia, Maria!')

# Função sem retorno e com parâmetro
def imprimir_nome(nome):
    print(f'Nome: {nome}!')

# Função com retorno e sem parâmetro
def gerar_saudacao():
    return 'Bom dia'

# Função com retorno e com parâmetro
def gerar_saudacao_para(nome):
    return f'Bom dia, {nome}!'

# Chamada
print('Olá')

imprimir_saudacao()

imprimir_nome('Maria')

print(gerar_saudacao())

print(gerar_saudacao_para('Júlio'))

# Argumentos nomeados
def nova_saudacao(nome, saudacao):
    return f'{saudacao}, {nome}!'



print(nova_saudacao('Joel', 'Bom dia'))
print(nova_saudacao(nome='Joel', saudacao='Boa tarde'))
print(nova_saudacao(saudacao='Boa noite', nome='Joel'))
