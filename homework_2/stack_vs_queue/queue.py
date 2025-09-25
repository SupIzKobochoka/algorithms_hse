from linkedlist import LinkedList

class Queue:
    def __init__(self):
        self.data = LinkedList()

    def push(self, value):
        self.data.add(value, 0)

    def pop(self):
        return self.data.pop(-1)


if __name__ == '__main__':
    from queque_tests import test

    test(Queue)

    