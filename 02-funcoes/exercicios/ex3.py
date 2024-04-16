# Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.

from unicodedata import normalize, category


def strip_accents(s: str):
   return ''.join(c for c in normalize('NFD', s) if category(c) != 'Mn')

def count_vowels_and_consonants(text: str):
    VOWELS = 'aeiou'
    CONSONANTS = 'qwrtypsdfghjklzxcvbnm'

    vowels = 0
    consonants = 0

    for char in text:
        if char in VOWELS:
            vowels += 1
        elif char in CONSONANTS:
            consonants += 1

    return {
        'vowels': vowels,
        'consonants': consonants,
    }


text = strip_accents(input('Digite uma frase: ').strip().lower())
vowels, consonants = count_vowels_and_consonants(text).values()

print(f'Nesta frase, temos {vowels} vogais e {consonants} consoantes')
