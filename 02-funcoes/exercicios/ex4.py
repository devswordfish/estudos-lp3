# Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. O programa deve pedir ao usuário para votar várias vezes e, no final, mostrar o número de votos de cada candidato e quem foi o vencedor.

def int_input(prompt: str):
    while True:
        try:
            number = int(input(prompt))
            break
        except:
            print('Digite um número!')
    return number

def find_winners(candidates_votes: dict[str, int]):
    max_votes = max(candidates_votes.values())

    return [candidate for candidate, votes in candidates_votes.items() if votes == max_votes]

def separate_list(lis: list[str]):
    new_text = ''
    length = len(lis)

    for i, value in enumerate(lis):
        new_text += value

        if i < length - 1:
            new_text += ', ' if i < length - 2 else ' e '

    return new_text

def print_candidates(candidates: list[str]):
    print('Escolha entre um dos candidatos para votar: ')
    print('[0] - terminar votação')
    for i, candidate in enumerate(candidates):
        print(f'[{i + 1}] - {candidate}')

def get_votings(candidates: list[str]):
    candidates_votes = {candidate: 0 for candidate in candidates}

    while True:
        option = int_input('Digite o número do candidato: ')

        if option == 0:
            break
        elif option < 0 or option > len(candidates):
            print('Opção inválida!')
        else:
            candidates_votes[candidates[option - 1]] += 1
    
    return candidates_votes

def simulate_elections(candidates: list[str]):
    print_candidates(candidates)

    candidates_votes = get_votings(candidates)

    print('-' * 30)

    for candidate, votes in candidates_votes.items():
        print(f'Candidato {candidate} - {votes} votos')

    print('-' * 30)

    winners = find_winners(candidates_votes)

    if len(winners) == 1:
        print(f'O vencedor dessa eleição é o candidato {winners[0]}')
    else:
        print(f'Empate entre os candidatos {separate_list(winners)}')


CANDIDATES = ['A', 'B', 'C']

simulate_elections(CANDIDATES)
