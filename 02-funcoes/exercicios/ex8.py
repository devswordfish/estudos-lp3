# Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes textos fornecidos pelo usuário.

from collections import Counter
import functools


def generate_frequency_dictionary(text: str):
    SEPARATORS = ',.!?(){}[]:;'

    for sep in SEPARATORS:
        text = text.replace(sep, ' ')

    splitted_text = text.split()

    return dict(Counter(splitted_text))

def show_frequency_dictionary_in_table(frequency_dictionary: dict[str, int]):
    if len(frequency_dictionary) == 0:
        print('Sem palavras')
        return

    longest_word_length = max([len(word) for word in frequency_dictionary.keys()])
    highest_frequency_length = len(str(max(frequency_dictionary.values())))

    print(f'-{'-' * longest_word_length}-+-{'-' * highest_frequency_length}-')

    sorted_frequency_dictionary = sorted(frequency_dictionary.items(), key=functools.cmp_to_key(custom_sorting))

    for word, freq in sorted_frequency_dictionary:
        print(f' {word:<{longest_word_length}} | {freq:<{highest_frequency_length}}')

def custom_sorting(x: tuple[str, int], y: tuple[str, int]):
    '''
        ordena por frequência e alfabeticamente    
    '''

    if x[1] > y[1]:
        return -1
    elif x[1] < y[1]:
        return 1
    elif x[0] > y[0]:
        return 1
    elif x[0] < y[0]:
        return -1
    return 0


text = input('Digite um texto: ')

freq_dict = generate_frequency_dictionary(text)
show_frequency_dictionary_in_table(freq_dict)
