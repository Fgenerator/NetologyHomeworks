def calculation(sign, a, b):
    try:
        calculations = {
            '+': int(a) + int(b),
            '-': int(a) - int(b),
            '*': int(a) * int(b),
            '/': int(a) / int(b)
        }
    except (ValueError, ZeroDivisionError) as e:
        print('Неверный тип аргументов.', e)
        main()
    try:
        assert sign in calculations.keys()
    except AssertionError:
        print('Недопустимая операция.')
        main()
    else:
        return calculations[sign]


def input_handling(user_input):
    user_input = user_input.split()
    try:
        print(calculation(*user_input))
    except TypeError:
        print('Передано неверное количество аргументов')
        main()


def main():
    while True:
        input_handling(input('Введите данные: '))


main()
