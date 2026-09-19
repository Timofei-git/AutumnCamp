class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.size += 1

    def delete(self, data):
        if self.head is None:
            return False


        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False

    def to_list(self):
        result = []
        if self.head is None:
            return result

        current = self.head
        while current.next is not None:
            result.append(current.data)
            current = current.next
        result.append(current.data)
        return result
    
    def reverse(self):
        if self.head == None:
            return
        
        prev = None
        current = self.head
        while current.next is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


lst = LinkedList()
lst.append(10)
lst.append(20)
lst.append(30)
lst.prepend(5)

print(lst.to_list())
lst.delete(20)
lst.reverse()
print(lst.to_list())