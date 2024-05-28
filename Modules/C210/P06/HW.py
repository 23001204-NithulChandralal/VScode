class Stack:
    def __init__(self):
        self.__data = []  

    def __str__(self):
        out_str = "Stack: " + stack
        out_str += "Is stack empty? : " + stack.isEmpty()
        out_str += "Stack after popping: " + stack
        return out_str

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if not self.isEmpty():
            popped_item = self.__data.pop()
            print("Popped item:", popped_item)
        else:
            print("Empty Sack!")

    def isEmpty(self):
        return len(self.__data) == 0

    def __len__(self):
        return len(self.__data)

# Testing the Stack class
stack = Stack()

# Pushing elements onto the stack
stack.push(5)
stack.push(10)
stack.push(15)





print("Stack length:", len(stack))  # Getting the length of the stack
print("Is stack empty now?", stack.isEmpty())  # Checking if the stack is empty after popping
