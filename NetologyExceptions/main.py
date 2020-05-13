def calculation(sign, a, b):
    if sign == '+':
        return addition(a, b)
    elif sign == '-':
        return subtraction(a, b)
    elif sign == '*':
        return multiplication(a, b)
    elif sign == '/':
        return division(a, b)


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на ноль.')
        main()


def input_handling(input):
    input = input.split()
    try:
        assert len(input) == 3
    except AssertionError:
        print('Передано неверное количество аргументов.')
        main()
    else:
        ops = ['+', '-', '*', '/']
        try:
            assert input[0] in ops
        except AssertionError:
            print('Недопустимая операция.')
            main()
        else:
            print(calculation(input[0], int(input[1]), int(input[2])))


def main():
    input_handling(input('Введите данные: '))


main()

