def calculation(sign, a, b):
    ops = ['+', '-', '*', '/']
    try:
        test = {
            '+': int(a) + int(b),
            '-': int(a) - int(b),
            '*': int(a) * int(b),
            '/': int(a) / int(b)
        }
    except(ValueError):
        print('Неверный тип аргументов.')
        main()
    try:
        assert sign in ops
    except AssertionError:
        print('Недопустимая операция.')
        main()
    else:
        try:
            return test[sign]
        except ZeroDivisionError:
                print('Деление на ноль.')
                main()


def input_handling(input):
    input = input.split()
    try:
        print(calculation(*input))
    except TypeError:
        print('Передано неверное количество аргументов')
        main()


def main():
    while True:
        input_handling(input('Введите данные: '))


main()

