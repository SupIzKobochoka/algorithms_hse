from linkedlist import LinkedList

class Stack:
    def __init__(self):
        self.data = LinkedList()

    def push(self, value):
        self.data.add(value, -1)

    def pop(self):
        return self.data.pop()

if __name__ == '__main__':
    from stack_tests import test

    test(Stack)

    


    
