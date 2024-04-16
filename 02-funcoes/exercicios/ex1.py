# Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

from random import randint


def print_divisor(text: str):
    divisor = '-' * (len(text) + 4)

    print(divisor)
    print('  ' + text)
    print(divisor)

def print_title(text: str):
    divisor = '#' * (len(text) + 4)

    print(divisor)
    print('# ' + text.upper() + ' #')
    print(divisor)

def int_input(prompt: str):
    while True:
        try:
            number = int(input(prompt))
            break
        except:
            print('Digite um número válido!')
    return number

def is_in_range(number: int, min_number: int, max_number: int):
    return min_number <= number <= max_number

def winning_messages(attempts: int):
    if attempts == 1:
        return 'UMA TENTATIVA!?? :O'
    elif attempts == 2:
        return 'De segunda! :)'
    elif attempts <= 5:
        return 'Boa!!!'
    elif attempts <= 12:
        return 'Boa!'
    elif attempts <= 20:
        return 'Acertou'
    return 'Zzzzzz...'

def guess_game_user_play(min_number: int, max_number: int):
    # computador escolhe um número aleatório entre (min_number, max_number)
    random_number = randint(min_number, max_number)
    print(random_number)

    attempts = 0
    giveup = False

    # início do jogo
    while True:
        # pega o palpite do usuário
        guess = int_input(f'Digite um número entre {min_number} e {max_number} (-1: desistir): ')

        # usuário desistiu da rodada em qualquer momento
        if guess == -1:
            giveup = True
            break

        # palpite estava fora do intervalo permitido
        if not is_in_range(guess, min_number, max_number):
            print(f'Digite um valor no ENTRE {min_number} e {max_number}!')
            continue

        attempts += 1

        # verifica se o usuário acertou o número do computador
        if guess == random_number:
            break
        elif guess > random_number:
            print_divisor('Digite um número menor!')
        else:
            print_divisor('Digite um número maior!')

    return {
        'attempts': attempts,
        'giveup': giveup
    }

def guess_game_ask_play_again():
    while True:
        option = input('Quer jogar de novo? (s/n) ').strip().lower()

        # usuário digitou uma opção válida
        if option == 's' or option == 'n':
            break

        print('Digite "s" ou "n"')
        print()
    
    return option == 's'

def guess_game(min_number: int, max_number: int):
    # verificações para fazer o jogo funcionar somente com valores não negativos e número mínimo < número máximo
    if min_number < 0:
        raise Exception(f'O número mínimo {min_number} não pode ser negativo')

    if max_number < 0:
        raise Exception(f'O número máximo {max_number} não pode ser negativo')

    if min_number > max_number:
        raise Exception(f'O número mínimo {min_number} não pode ser maior que o máximo {max_number}')

    # mostra o nome do jogo
    print_title('jogo de adivinhação')
    print()

    keep_playing = True

    while keep_playing:
        # computador escolhe um número aleatório entre (min_number, max_number)
        random_number = randint(min_number, max_number)

        attempts = 0
        giveup = False

        # início do jogo
        while True:
            # pega o palpite do usuário
            guess = int_input(f'Digite um número entre {min_number} e {max_number} (-1: desistir): ')

            # usuário desistiu da rodada em qualquer momento
            if guess == -1:
                giveup = True
                break

            # palpite estava fora do intervalo permitido
            if not is_in_range(guess, min_number, max_number):
                print(f'Digite um valor no ENTRE {min_number} e {max_number}!')
                continue

            attempts += 1

            # verifica se o usuário acertou o número do computador
            if guess == random_number:
                break
            elif guess > random_number:
                print_divisor('Digite um número menor!')
            else:
                print_divisor('Digite um número maior!')

        # mostra os resultados do jogo
        print()
        print(f'Tentativas: {attempts}')

        if giveup:
            print_divisor('Desistiu! :(')
        else:
            print_divisor(winning_messages(attempts))

        print()

        # pergunta se o usuário quer continuar jogando
        while True:
            option = input('Quer jogar de novo? (s/n) ').strip().lower()

            # usuário digitou uma opção válida
            if option == 's' or option == 'n':
                break

            print('Digite "s" ou "n"')
            print()
        
        if option == 's':
            print('-' * 30)
        else:
            keep_playing = False


MIN_NUMBER = 1
MAX_NUMBER = 100

guess_game(MIN_NUMBER, MAX_NUMBER)
