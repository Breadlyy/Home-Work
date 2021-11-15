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
     price = item.price
     length = 0
     if self.head is not None:
      while length <= self.count:
          if item.price <= self.head.data.price:
              item, self.head = self.head, item;
          self.count-=1;
     if  item.price > price:
          self.head = NewNode
          cost = item.price;
     else:
         self.head = NewNode;
         cost = item.price;
     self.count+= 1



    def updateName(self, identification, name):
        while True:
             if identification == self.count:
                self.head.name = name
                break;  
             elif identification >= self.count:
              return None;
             self.count-=1;
        
    def updateBrand(self, identification, brand):
     while True:
            if identification == self.count:
                self.head.name = brand
                break;  
            elif identification >= self.count:
                return None;
            self.count-=1;
        
    def activateCar(self, identification):
        while True:
         if identification == self.count:
            self.head.active = 1;
            break;
         elif identification >= self.count:
             return None
         self.count-=1;
        

    def deactivateCar(self, identification):
        pass
    
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
         

def init(cars):
  for i in range(len(cars) - 1):
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
car1 = Car(1, "RAM", "Dodge", 10000, 1);
car2 = Car(2, "Skoda", "Superb", 8000, 1);
car3 = Car(3, "Lada", "Priora", 2000, 1);
car4 = Car(4, "Lada", "Granta", 4000, 1);
cars = [car1, car2, car3,car4];
for i in range(len(cars)):
    print(cars[i].price);
    


init(cars);


db.print_();

