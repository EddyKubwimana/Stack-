class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)
    def pop(self):
        return self.data.pop()
    def peep(self):
        print(self.data[len(self.data)-1])
stack = Stack()
stack.push(3)
stack.push(6)
stack.push(7)
stack.peep()
stack.pop()

stack.peep()
