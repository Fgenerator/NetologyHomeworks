class Stack:
    def __init__(self) -> None:
        self.data = []

    def is_empty(self) -> bool:
        return self.data == []

    def push(self, item: any) -> None:
        self.data.append(item)

    def pop(self) -> any:
        return self.data.pop()

    def peek(self) -> any:
        return self.data[len(self.data)-1]

    def size(self) -> int:
        return len(self.data)


def balance_string(string):
    ...


if __name__ == '__main__':
    stack = Stack()
    print(stack.is_empty())
    print(stack.size())

    stack.push(1)
    stack.push(2)
    stack.push(5)

    print(stack.is_empty())
    print(stack.size())

    print(stack.peek())

    print(stack.pop())

    print(stack.size())

