class Node:
    def __init__(self,nextNode, prevNode,item):
        self.nextNode = nextNode;
        self.prevNode = None;
        self.item = None;

class LinkedList:
    def __init__(car):
        car.head = None
        car.start = None
        car.count = 0

    def getDatabase(car):
        return car.count;
    def getDatabaseHead():
        pass  

    def clean():
        LinkedList.clean()

    def add(car):
        node = Node()
        

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


db = LinkedList()


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
