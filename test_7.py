import functools
import queue
import threading 

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

     def printItems(self):
         i = 1
         while i <= len(self.items):
             print(self.items[len(self.items) - i])
             i+=1

             
         

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

    def printQueue(self):
        for i in range(len(self.items) -1 ):
            print(self.items[i]);
class car:
      def __init__(self, brand, price):
         self.brand = brand;
         self.price = price;
      def __str__(self):
        print(self.brand + " " + self.price);




stack = Stack();
queue = Queue();
C1 = car("BMW", "750000");
C2 = car("Tatra", "500000");
C3 = car("Lada", "300000");
C4 = car("Honda", "700000");
queue.enqueue(C1);
queue.enqueue(C2);
queue.enqueue(C3);
queue.enqueue(C4);


stack.push(C1);
stack.push(C2);
stack.push(C3);
stack.push(C4);

stack.printItems()



