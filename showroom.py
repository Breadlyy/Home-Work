class Node:
    def __init__(self, item, nextNode = None, prevNode = None):
        self.nextNode = nextNode;
        self.prevNode = prevNode;
        self.item = item;

class LinkedList(object):
    def __init__(car):
        car.head = None
        car.start = None
        car.count = 0

    def getDatabase(self):
        return car.count;
    def getDatabaseHead(self):
        return self.head;

    def clean():
        LinkedList.clean()

    def add(self, item):
        NewNode = Node(item);
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = self.head
            self.head = NewNode
        self.count+= 1

    def updateName(self, identification, name):
        if identification == self.count:
            self.head.name = name
        self.count-=1
        
    def updateBrand(self, identification, brand):
        if identification == self.count:
                self.head.name = brand
        self.count-= 1;
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


class car:
      def __init__(self, name: str, brand: str, price: int, active: bool):
         self.name = name;
         self.brand = brand;
         self.price = price;
         self.active = active;
         
      def __str__(self):
        print(self.brand + " " + self.price);


bd = LinkedList()


def init(cars):
    pass


def add(car):
    pass


def updateName(identification, name):
    pass


def updateBrand(identification, brand):
    pass


def activateCar(identification):
    pass


def deactivateCar(identification):
    pass


def getDatabaseHead():
    pass


def getDatabase():
    pass


def calculateCarPrice():
    pass


def clean():
    pass
