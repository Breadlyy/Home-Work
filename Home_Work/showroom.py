class Node:
    prevNode = None
    nextNode = None
    data = None
    
    def __init__(self, data, nextNode=None, prevNode=None):
        self.data = data
        self.nextNode = nextNode
        self.prevNode = prevNode
        

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        elif self.head.data.price > new_node.data.price:
            new_node.nextNode = self.head
            new_node.nextNode.prevNode = new_node
            self.head = new_node

        else:
            current = self.head
            
            while (current.nextNode != None) and (current.nextNode.data.price <= new_node.data.price):
                current = current.nextNode

            new_node.nextNode = current.nextNode
            if current.nextNode != None:
                new_node.nextNode.prevNone = new_node

            current.nextNode = new_node
            new_node.prevNode = current

    
    def updateName(self, identification, name):
        if self.head:
            current = self.head
            while current != None:
                if current.data.identification == identification:
                    current.data.name = name
                    break
                current = current.nextNode


    def updateBrand(self, identification, brand):
        if self.head:
            current = self.head
            while current != None:
                if current.data.identification == identification:
                    current.data.brand = brand
                    break
                current = current.nextNode


    def activateCar(self, identification):
        if self.head:
            current = self.head
            while current != None:
                if current.data.identification == identification:
                    current.data.active = True
                    break
                current = current.nextNode
            


    def deactivateCar(self, identification):
        if self.head:    
            current = self.head
            while current != None:
                if current.data.identification == identification:
                    current.data.active = False
                    break
                current = current.nextNode


    def getDatabaseHead(self):
        return db.head


    def getDatabase(self):
        return db


    def calculateCarPrice(self):
        sum = 0
        current = self.head
        while current != None:
            if current.data.active == True:
                sum += current.data.price
            current = current.nextNode
        return sum

        
    def clean(self):
        while self.head != None:
            temp = self.head
            self.head = self.head.nextNode
            temp = None
        print("All nodes are deleted successfully.")

    def printList(self):
        if self.head:
            node = self.head
            while node:
                print(str(node.data), end = "\n")
                node = node.nextNode
        else:
            print('List is empty')


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification
        self.name = name
        self.brand = brand
        self.price = price
        self.active = active

    def __str__(self):
        return str(self.identification) + " " + self.name + " " + self.brand + " " + str(self.price) + " " + str(self.active)

db = LinkedList()

def init(cars):
    for car in cars:
        db.add(car)
    
def add(car):
    db.add(car)

def updateName(identification, name):
    db.updateName(identification, name)


def updateBrand(identification, brand):
    db.updateBrand(identification, brand)


def activateCar(identification):
    db.activateCar(identification)


def deactivateCar(identification):
    db.deactivateCar(identification)


def getDatabaseHead():
    return db.getDatabaseHead()


def getDatabase():
    return db.getDatabase()


def calculateCarPrice():
    return db.calculateCarPrice()


def clean():
    db.clean()

