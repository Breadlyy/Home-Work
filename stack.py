class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return (self.items == [])


def parChecker(symbolString):
    s = Stack()
    for symbol in symbolString:
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.isEmpty():
                return False
            else:
                s.pop()
    return s.isEmpty()




s = Stack()
s.push("dela")
s.push("to")
s.push("co")
s.push("vime")

while not s.isEmpty():
    print(s.pop())

print(parChecker("(3+(2*(-2)+(3*5)-1)/(3-2)*2)"))
print(parChecker("((3+2)+(5*8)*(4)"))