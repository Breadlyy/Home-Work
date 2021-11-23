class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None
        self.count = 0

    def isEmpty(self):
        return self.head is None

    def push(self,item):
        node = Node(item)
        if not self.head:
            self.head = self.end = node
        else:
            node.next = self.head
            self.head = node
        self.count +=1

    def pop(self):
        if self.head:
            ret = self.head.data
            self.head = self.head.next
            if self.head == None:
                self.end = None
            self.count -=1
            return ret

    def pushEnd(self, item):
        node = Node(item)
        if not self.end:
            self.head = self.end = node
        else:
            self.end.next = node
            self.end = node
        self.count +=1

    def popEnd(self):
        if self.head:
            self.count -=1
            ret = self.end.data
            if self.head == self.end:
                self.head = self.end = None
            else:
                cur = self.head
                while cur.next != self.end:
                    cur = cur.next
                self.end = cur
                self.end.next = None
            return ret


    def size(self):
#        current = self.head
#        count = 0
#        while current != None:
#            count += 1
#            current = current.next
#        return count
        return self.count


    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next


myL = LinkedList()
myL.push(1)
myL.push(2)
myL.pushEnd(3)

print(myL.search(2))
myL.remove(2)
print(myL.search(2))

while not myL.isEmpty():
    print(myL.pop())
