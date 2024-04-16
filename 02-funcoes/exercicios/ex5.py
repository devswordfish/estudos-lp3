# Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).

from unicodedata import normalize, category


def strip_accents(s: str):
   return ''.join(c for c in normalize('NFD', s) if category(c) != 'Mn')

def is_palindrome(string: str):
    string = strip_accents(string.strip().lower())

    alphanumeric_string = ' '.join([char for char in string if char.isalnum()])

    return alphanumeric_string == alphanumeric_string[::-1]


string = input('Digite uma palavra: ')

is_palindrome_text = 'é um palíndromo' if is_palindrome(string) else 'não é um palíndromo'

print('A palavra digitada ' + is_palindrome_text)
