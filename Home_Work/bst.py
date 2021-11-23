class Node:
    def __init__(self, value=None):
        self.left_child = None;
        self.right_child = None;
        self.parent = None # pointer to parent
        self.value = value;

class BinarySearchTree:
    def __init__(self):
        self.root = None;
        self.vis = 0;
        self.size = 0;

    def _insert(self,value,cur_node):
         if value < cur_node.value:
             if cur_node.left_child==None:
                 cur_node.left_child=Node(value)
                 cur_node.left_child.parent=cur_node # set parent
             else:
                 self._insert(value, cur_node.left_child)
         elif value > cur_node.value:
             if cur_node.right_child == None:
                 cur_node.right_child = Node(value);
                 cur_node.right_child.parent = cur_node
             else:
                self._insert(value, cur_node.right_child)
                
    def insert(self, value):
        self.size+=1
        if self.root==None:
    	    self.root=Node(value)
        else:
         self._insert(value, self.root);
	                
    def fromArray(self, array):
      for i in range(len(array)):
          self.insert(array[i]);

    def search(self, value):
     self.vis = 0
     if self.root is not None:
        return self._search(value, self.root)
     else:
         return False
    
    def _search(self, value, cur_node):
        self.vis+=1
        if value == cur_node.value: 
           return True
        elif value > cur_node.value and cur_node.right_child is not None: 
           return self._search(value, cur_node.right_child) 
        elif value < cur_node.value  and cur_node.left_child is not None:
           return self._search(value, cur_node.left_child) 
        else: return False
        
    def min(self):
        self.vis = 0
        if self.root is not None:
           return self._min(self.root)
    
    def _min(self, cur_node):
        self.vis+=1
        while cur_node.left_child is not None:
            self.vis+=1
            cur_node = cur_node.left_child
        return cur_node.value;

    def max(self):
        self.vis = 0
        if self.root is not None:
          return self._max(self.root)
      
    def _max(self, cur_node):
        self.vis+=1
        while cur_node.right_child is not None:
            self.vis+=1
            cur_node = cur_node.right_child
        return cur_node.value;

    def visitedNodes(self):
        VisitedNodes = self.vis;
        self.vis = 0
        return VisitedNodes;


value_1 = 5;
value_2 = 8;
value_3 = 2;
value_4 = 12;
bst = BinarySearchTree();
bst.fromArray([8, 3, 4,13, 46,77,10, 1, 7, 6])
bst.min()
print(bst.visitedNodes())
bst.max()
print(bst.visitedNodes())



