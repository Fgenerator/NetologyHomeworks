import operator


def calculation(sign, a, b):
    calculations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
    try:
        assert sign in calculations.keys()
    except AssertionError:
        print('Недопустимая операция.')
        main()
    else:
        try:
            return calculations[sign](int(a), int(b))
        except ValueError:
            print('Неверный тип аргументов.')
            main()
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
