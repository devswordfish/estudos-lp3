# Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

def float_input(prompt: str):
    while True:
        try:
            number = float(input(prompt))
            break
        except:
            print('Digite um número válido!')
    return number

def convert_grade_number_to_letter(grade: int, max_grade: int):
    if grade >= max_grade * 0.8:
        return 'A'
    elif grade >= max_grade * 0.6:
        return 'B'
    elif grade >= max_grade * 0.4:
        return 'C'
    elif grade >= max_grade * 0.2:
        return 'D'
    return 'F'

def show_grades(grades: list[tuple[int, str]]):
    print('NOTAS CONVERTIDAS')
    for grade_number, grade_letter in grades:
        print(f'{grade_number:6.2f} | {grade_letter:^8}')

def ask_grades(total_grades: int):
    grades = []

    for i in range(1, total_grades + 1):
        grade = float_input(f'Digite a sua {i}ª nota: ')

        grades.append(grade)

    return grades


GRADES = 4

grades = ask_grades(GRADES)
converted_grades = [convert_grade_number_to_letter(grade, max_grade=100) for grade in grades]

print()
show_grades(list(zip(grades, converted_grades)))
