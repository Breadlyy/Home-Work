class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.enqueue("dela")
q.enqueue("to")
q.enqueue("co")
q.enqueue("vime")

while not q.isEmpty():
    print(q.dequeue())


