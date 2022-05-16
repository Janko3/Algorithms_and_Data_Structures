import queue


class EmptyQueue(Exception):
    pass


class FullQueue(Exception):
    pass


class ArrayQueue(object):

    def __init__(self):
        DEFAULT_CAPACITY = 10
        self._data = [None] * DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def _len_(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size > len(self._data)

    def first(self):
        if self.isEmpty():
            raise EmptyQueue("Red je prazan")

        return self._data[self._front]

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1+walk) % len(old)
        self._front = 0

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueue("Red je prazan")
        first = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return first

    def enqueu(self, el):
        if self._size == len(self._data):
            self._resize(2*len(self._data))

        availible = (self._front + self._size) % len(self._data)
        self._data[availible] = el
        self._size += 1

    def __str__(self):
        return str(self._data)


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, el):
        self._data.append(el)

    def top(self):
        if self.is_empty():
            raise EmptyQueue("Stek je prazan")
        else:
            return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise EmptyQueue("Stek je prazan")
        return self._data.pop()

    def __str__(self):
        return str(self._data)


def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


class Deque:

    def __init__(self, capacity=10):
        self._data = [None]*capacity
        self._first = 0
        self._size = 0
        self._capacity = capacity

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def first(self):
        if self.is_empty():
            raise EmptyQueue("Deque je prazan")
        return self._data[self._first]

    def last(self):
        if self.is_empty():
            raise EmptyQueue("Deque je prazan")
        last = (self._first + self._size - 1) % self._capacity
        return self._data[last]

    def add_last(self, el):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        index = (self._first + self._size) % self._capacity
        self._data[index] = el
        self._size += 1

    def add_first(self, el):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        index = (self._first - 1) % self._capacity
        self._first = (self._first - 1) % self._capacity
        self._data[index] = el
        self._first = index
        self._size += 1

    def remove_first(self):
        el = self._data[self.first]
        self._data[self._first] = None
        self._first = (self._first + 1) % self._capacity

    def remove_last(self):
        if self.is_empty():
            raise EmptyQueue("Deque je prazan")
        index = (self._first + self._size - 1) % self._capacity
        el = self._data[index]
        self._data[index] = None
        self._size -= 1

    def enqueue(self, el):
        if self._size == self._capacity:
            self._resize(2*self._capacity)
        last = (self._first + self._size) % self._capacity
        self._data[last] = el
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueue("Deque je prazan")
        el = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % self._capacity
        self._size -= 1
        if self._size < self._capacity//4:
            self._resize(self._capacity//2)
        return el

    def _resize(self, cap):
        current_data = self._data
        current_first = self._first
        self._data = [None] * cap
        for i in range(self._size):
            self._data[i] = current_data[current_first]
            current_first = (current_first + 1) % self._capacity
        self._first = 0
        self._capacity = cap


if __name__ == "__main__":
    queue = ArrayQueue()
    queue.enqueu(3)
    queue.enqueu(5)
    print(queue)

    queue.dequeue()
    print(queue)

    expr = '(())'
    print(is_matched(expr))
