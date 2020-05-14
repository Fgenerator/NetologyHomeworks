def calculation(sign, a, b):
    ops = ['+', '-', '*', '/']
    try:
        calculations = {
            '+': int(a) + int(b),
            '-': int(a) - int(b),
            '*': int(a) * int(b),
            '/': int(a) / int(b)
        }
    except ValueError:
        print('Неверный тип аргументов.')
        main()
    try:
        assert sign in ops
    except AssertionError:
        print('Недопустимая операция.')
        main()
    else:
        try:
            return calculations[sign]
        except ZeroDivisionError:
            print('Деление на ноль.')
            main()


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
