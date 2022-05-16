class EmptyList(Exception):
    pass


class Node(object):

    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __str__(self):
        return str(self._value)


class SinglyLinkedList(object):

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def __iter__(self):
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node.next

    def get_last(self):
        if self.is_empty():
            raise EmptyList("Prazna lista")
        return self._tail

    def add_last(self, value):
        node = Node(value)
        if self.is_empty():
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def remove_last(self):
        pop = None
        if self.is_empty():
            raise EmptyList("Prazna lista")
        if self._size == 1:
            self._head = pop
            self._size -= 1
            self._head = None
        for node in self:
            if node.next == self._tail:
                pop = node.next
                node.next = None
                self._tail = node
                self._size -= 1
                return pop


class EmptyStack(Exception):
    pass


class UnlimitedStack:

    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return self._data._size

    def is_empty(self):
        return self._data.is_empty()

    def top(self):
        if self.is_empty():
            raise EmptyStack("Prazan stek")
        return self._data.get_last()

    def push(self, value):
        self._data.add_last(value)

    def pop(self):
        if self.is_empty():
            raise EmptyStack("Prazan stek")
        return self._data.remove_last()


if __name__ == "__main__":
    s = UnlimitedStack()
    s.push(3)
    s.push(5)
    print(s.top())
    print(s.pop())
    print(s.top())
