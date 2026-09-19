# Реализуй класс DoublyLinkedList с методами append, prepend, remove(node) и to_list. Проверь: добавь 10, 20, 30, потом удали средний узел и выведи результат.

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1
        return node

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def remove(self, node):
        if self.head is None:
            return False

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.length -= 1
        return True

    def to_list(self):
        result = []
        current = self.head
        if self.head is None:
            return result
        while current is not None:
            result.append(current.value)
            current = current.next

        return result
# Добавь метод to_list_reversed(), который собирает элементы с конца к началу, и метод insert_after(node, value),
    # вставляющий новый узел сразу после указанного. Проверь оба на списке из четырёх элементов.
    def to_list_reversed(self):
        result = []
        current  = self.tail
        if self.head is None:
            return result
        while current is not None:
            result.append(current.value)
            current = current.prev

        return result

    def insert_after(self, node, value):
        node_1 = Node(value)
        if self.head is None:
            return False

        current = self.head
        while current is not None:
            if current == node:
                self.length += 1
                node_1.next = current.next
                current.next = node_1
                node_1.prev = current
                if node_1.next is not None:
                    node_1.next.prev = node_1
                else:
                    self.tail = node_1
                return True
            current = current.next

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(10)
node_sr = doubly_linked_list.append(20)
doubly_linked_list.insert_after(node_sr, 30)
print(doubly_linked_list.to_list())
