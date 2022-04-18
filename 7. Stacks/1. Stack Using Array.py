class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!")
            return
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Hey! Stack is Empty!")
            return
        return self.__data[len(self.__data)-1]

    def size(self, item):
        return len(self.__data)

    def isEmpty(self):                              # size() to check weather length of array is zero or not
        return self.size(len(self.__data)) == 0

s = Stack()

s.push(12)
s.push(13)
s.push(14)

while s.isEmpty() is False:
    print(s.pop())

s.top()

