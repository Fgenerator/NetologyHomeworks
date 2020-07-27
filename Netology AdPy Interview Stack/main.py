class Stack:
    def __init__(self) -> None:
        self.data = []

    def is_empty(self) -> bool:
        return self.data == []

    def push(self, item: any) -> None:
        self.data.append(item)

    def pop(self) -> any:
        if not self.is_empty():
            return self.data.pop()

    def peek(self) -> any:
        if not self.is_empty():
            return self.data[len(self.data)-1]

    def size(self) -> int:
        return len(self.data)


def balance_string(string: str) -> str:
    conformity = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    brackets = ['{', '}', '[', ']', '(', ')']

    stack = Stack()

    for symbol in string:
        if symbol in brackets:
            if symbol in conformity.values():
                stack.push(symbol)
            else:
                if conformity[symbol] != stack.peek():
                    return 'String is unbalanced'
                else:
                    stack.pop()
    if stack.is_empty():
        return 'String is balanced'
    else:
        return 'String is unbalanced'


# завести пустой стек
#
# для каждого символа строки
#   если он присутствует в наборе скобок
#     если он отсутствует в словаре соответствий, т. е. это открывающая скобка
#       добавить в стек этот символ
#     иначе он закрывающая скобка
#       если значение из словаря соответствий отличается от вершины стека
#         return false
#       иначе
#         выкинуть последний элемент стека
#
# return стек пуст

if __name__ == '__main__':
    print(balance_string('(((([{}]))))'))
    print(balance_string('[([])((([[[]]])))]{()}'))
    print(balance_string('{{[()]}}'))
    print()
    print(balance_string('}{}'))
    print(balance_string('{{[(])]}}'))
    print(balance_string('[[{())}]'))



