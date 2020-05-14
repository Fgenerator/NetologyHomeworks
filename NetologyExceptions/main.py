def calculation(sign, a, b):
    ops = ['+', '-', '*', '/']
    try:
        assert sign in ops
    except AssertionError:
        print('Недопустимая операция.')
        main()
    else:
        if sign == '+':
            return a + b
        elif sign == '-':
            return a - b
        elif sign == '*':
            return a * b
        elif sign == '/':
            try:
                return a / b
            except ZeroDivisionError:
                print('Деление на ноль.')
                main()


def input_handling(input):
    input = input.split()
    #print(calculation(input[0], int(input[1]), int(input[2])))
    try:
        print(calculation(*input))
    except TypeError:
        print('Передано неверное количество аргументов')
        main()


def main():
    input_handling(input('Введите данные: '))


main()

