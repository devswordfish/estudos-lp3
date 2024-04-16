# Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

def int_input(prompt: str):
    while True:
        try:
            number = int(input(prompt))
            break
        except:
            print('Digite um número inteiro válido!')
    return number

def print_multiplication_table(number: int):
    print('A tabuada desse número: ')
    for i in range(1, 11):
        print(f'{number} x {i:2} = {number * i}')


number = int_input('Digite um número inteiro: ')
print_multiplication_table(number)
