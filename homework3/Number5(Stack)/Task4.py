# Реализуй класс Stack с методами push, pop, peek, is_empty и поддержкой len(). Позаботься о понятной ошибке при попытке снять элемент с пустого стека.


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def length(self):
        return len(self._items)

stack = Stack()
print(stack.pop())
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.push(4)
stack.push(5)
print(stack.length())
print(stack.peek())

