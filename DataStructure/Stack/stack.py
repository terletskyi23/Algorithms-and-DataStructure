class Stack:

    def __init__(self):
        self.__stack = [];

    def isEmpty(self):
        return self.__stack == [];

    def push(self, data):
        self.__stack.append(data);

    def peek(self):
        return self.__stack[-1]

    def pop(self):
        data = self.__stack[-1]
        del self.__stack[-1]
        return data

    def sizeStack(self):
        return len(self.__stack);


# ----

stack = Stack();
stack.push(1);
stack.push(2);
stack.push(3);

print(stack.sizeStack());
print("Poped:  %s" % stack.pop());
print("Poped:  %s" % stack.pop());

print(stack.sizeStack());
print("Peeked:  %s" % stack.peek());
