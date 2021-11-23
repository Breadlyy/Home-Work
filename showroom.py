class Node:
     def __init__(self, data, nextNode = None, prevNode = None):
        self.nextNode = nextNode;
        self.prevNode = prevNode;
        self.data = data;

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def getDatabase(self):
        return LinkedList;

    def getDatabaseHead(self):
        return self.head;

    def clean(self):
        LinkedList.clean()

    def add(self, item):
     NewNode = Node(item);
     currentCount = self.count
     self.count+=1
     currentValue = self.head;
     if self.head is not None:
          if self.head.price < item.price:
                 self.nextNode = self.head
                 self.head = item
          while (self.nextNode is not None) and (currentValue.price >= item.price):
             currentValue = self.nextNode
          self.nextNode = item;
          self.prevNode = currentValue;     
     else:
         self.head = item;
         self.nextNode = self.tail
    #  p = self.head
    # while (p.next_name != self.tail) and (p.next_name.name < name):
    #       p = p.next_name
    # node.next_name = p.next_name
    # node.prev_name = p
    # p.next_name = node
    # node.next_name.prev_name = node



    def updateName(self, identification, name):
        while True:
             if identification == self.head.identification:
                self.head.name = name
                break;  
             elif identification != self.head.identification:
                self.head = self.nextNode
        
    def updateBrand(self, identification, brand):
     while True:
             if identification == self.head.identification:
                self.head.brand = brand
                break;  
             elif identification != self.head.identification:
                self.head = self.nextNode
        
    def activateCar(self, identification):
        while True:
             if identification == self.head.identification:
                self.head.activate = 1
                break;  
             elif identification != self.head.identification:
                self.head = self.nextNode
        

    def deactivateCar(self, identification):
        while True:
             if identification == self.head.identification:
                self.head.activate = 0
                break;  
             elif identification != self.head.identification:
                self.head = self.nextNode
    
    def calculateCarPrice(self):
        pass
    def isEmpty(self):
        return self.head is None

    def size(self):
     return self.count;

    def print_(self):
        temp_node = self.head
        while self.count != 0:
            print(temp_node);
            self.count-=1;
        


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = identification;
        self.name = name;
        self.brand = brand;
        self.price = price;
        self.active = active;
         

def _init_(cars):
  for i in range(len(cars)):
      db.add(cars[i]);

def add(car):
   db.add(car);


def updateName(identification, name):
    db.updateName(identification, name)


def updateBrand(identification, brand):
    db.updateName(identification, brand)


def activateCar(identification):
    db.activateCar(identification);


def deactivateCar(identification):
    db.deactivateCar(identification)


def getDatabaseHead():
    db.getDatabaseHead()


def getDatabase():
    db.getDatabase();


def calculateCarPrice():
    db.calculateCarPrice();


def clean():
    db.clean()    

db = LinkedList()
car1 = Car(1, "RAM", "Dodge", 12000, 1);
car2 = Car(2, "Skoda", "Superb", 8000, 1);
car3 = Car(3, "Lada", "Priora", 10000, 1);
car4 = Car(4, "Lada", "Granta", 4000, 1);
cars = [car1, car2, car3,car4];
for i in range(len(cars)):
    print(cars[i].price);
    


_init_(cars);


