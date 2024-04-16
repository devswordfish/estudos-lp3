# Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. O programa começa com uma palavra oculta (o usuário não vê) e o usuário tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado de tentativas para adivinhar toda a palavra.

from random import choice
from os import system, name
from unicodedata import normalize, category


def strip_accents(s: str):
   return ''.join(c for c in normalize('NFD', s) if category(c) != 'Mn')

def clear():
    if name == 'nt': # windows
        system('cls')
    else: # mac e linux
        system('clear')

def print_hangman_drawing(lives: int):
    hangman_drawings = {
        6: '+--+\n|  |\n|\n|\n|\n',
        5: '+--+\n|  |\n|  O\n|\n|\n',
        4: '+--+\n|  |\n|  O\n|  |\n|\n',
        3: '+--+\n|  |\n|  O\n| /|\n|\n',
        2: '+--+\n|  |\n|  O\n| /|\\\n|\n',
        1: '+--+\n|  |\n|  O\n| /|\\\n| /\n',
        0: '+--+\n|  |\n|  O\n| /|\\\n| / \\\n',
    }

    if lives > 6:
        lives = 6
    elif lives < 0:
        lives = 0

    print(hangman_drawings[lives])

def get_visible_word(original_word: str, normalized_word: str, letters_guessed: list[str]):
    word_visible = ''

    for i, char in enumerate(normalized_word):
        if not char.isalpha() or char in letters_guessed:
            word_visible += original_word[i]
        else:
            word_visible += '_'

        word_visible += ' '

    return word_visible

def is_word_finished(normalized_word: str, letters_guessed: list[str]):
    return not any([c for c in normalized_word if c not in letters_guessed])

def get_letter(letters_guessed: list[str]):
    while True:
        letter = strip_accents(input('Digite uma letra: ').strip().lower())

        if not letter.isalpha() or len(letter) != 1:
            print('Digite uma LETRA!')
        elif letter in letters_guessed:
            print('Você já escolheu essa letra!')
        else:
            return letter

def print_game_interface(lives: int, word: str, normalized_word: str, letters_guessed: list[str], theme: str):
    clear()
    print_hangman_drawing(lives)
    print(get_visible_word(word, normalized_word, letters_guessed))
    print(f'Letras escolhidas: {' '.join(letters_guessed)}')
    print(f'Tema: {theme}')

def hangman_game(words: list[dict[str, str]]):
    keep_playing = True

    while keep_playing:
        # computador escolhe uma palavra aleatória
        word_info = choice(words)

        word, theme = word_info.values()

        normalized_word = strip_accents(word.lower())
        lives = 6
        letters_guessed = []

        # jogo só acaba quando o usuário acertar a palavra ou o stickman for enforcado
        while lives > 0 and not is_word_finished( normalized_word, letters_guessed):
            print_game_interface(lives, word, normalized_word, letters_guessed, theme)
            print()

            letter = get_letter(letters_guessed)

            letters_guessed.append(letter)

            if letter not in normalized_word:
                lives -= 1

        print_game_interface(lives, word, normalized_word, letters_guessed, theme)
        print()

        if lives > 0:
            print('Você venceu!')
        else:
            print(f'Você perdeu! A palavra era {word}')

        print()

        # pergunta se o usuário quer continuar jogando (resposta deve ser obrigatoriamente 's' ou 'n')
        while True:
            option = input('Quer jogar de novo? (s/n) ').strip().lower()

            if option == 's':
                break
            elif option == 'n':
                keep_playing = False
                break
            else:
                print('Digite "s" ou "n"')
                print()

def create_hangman_word(word: str, theme: str):
    if not word:
        raise Exception('A palavra do jogo da forca não pode ser criada, porque a "palavra" não foi dada')
    
    if not theme:
        raise Exception('A palavra do jogo da forca não pode ser criada, porque o "tema" não foi dado')

    return {
        'word': word,
        'theme': theme,
    }


DATABASE_WORDS = [
    create_hangman_word('pneumoultramicroscopicossilicovulcanoconiótico', 'maior palavra da língua portuguesa'),
    create_hangman_word('Instituto Federal de Educação, Ciência e Tecnologia de São Paulo', 'instituto'),
    create_hangman_word('cachorro', 'animal'),
    create_hangman_word('lagosta', 'animal'),
    create_hangman_word('Brasil', 'país'),
    create_hangman_word('Chile', 'país'),
    create_hangman_word('Togo', 'país'),
    create_hangman_word('feijoada', 'comida'),
    create_hangman_word('banana', 'fruta'),
    create_hangman_word('caqui', 'fruta'),
    create_hangman_word('pitaya', 'fruta'),
]

hangman_game(DATABASE_WORDS)
