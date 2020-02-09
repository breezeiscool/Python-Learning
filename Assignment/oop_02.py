class Stack:
    def __init__(self):
        self.items = list()

    def clear(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
        return print(True) #for monitoring the implement

    def pop(self):
        # Judge whether the stack is empty or not before popping.
        if self.items:
            pop = self.items.pop()
            return pop
        else:
            return False

    def peek(self):
        # Return to the top item on the stack without removing it.
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        # Returns True if the stack is empty or False otherwise.
        return len(self.items) == 0

# test for the creating the class "stack"
test=Stack()
print(test.pop())
test.push(1)
test.push(2)
test.push(3)
print(test.pop())
print(test.peek())
print(test.isEmpty())
print(test.size())


