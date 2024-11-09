#1 - Linear search

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

#2 - Binary search in a sorted array

def binary_search_in_sorted_array(arr, key):
    
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#3 - Binary search tree

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def insert_into_BST(root, key):
    
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert_into_BST(root.right, key)
        else:
            root.left = insert_into_BST(root.left, key)
    return root

def array_to_bst(arr):

    if len(arr) == 0:
        return None
    
    root = None
    for key in arr:
        root = insert_into_BST(root, key)
    return root

def search_binary_search_tree(root, key):
    
    while root is not None:
        if root.val == key:
            return root
        elif root.val < key:
            root = root.right
        else:
            root = root.left
    return -1

#4 - Red-Black tree

class Node():
    def __init__(self,val):
        self.val = val                                   
        self.parent = None                             
        self.left = None                               
        self.right = None                              
        self.color = 1                                 

class RBTree():
    def __init__(self):
        self.NULL = Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL

    # Insert New Node
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                  

        y = None
        x = self.root

        while x != self.NULL :                       
            y = x
            if node.val < x.val :
                x = x.left
            else :
                x = x.right

        node.parent = y                                 
        if y == None :                                  
            self.root = node
        elif node.val < y.val :                       
            y.left = node
        else :
            y.right = node

        if node.parent == None :                      
            node.color = 0
            return

        if node.parent.parent == None :               
            return
        self.fixInsert ( node )                      

    # Left rotate
    def LR ( self , x ) :
        y = x.right                                      
        x.right = y.left                                
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent                          
        if x.parent == None :                        
            self.root = y                              
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y

    # Right rotate
    def RR ( self , x ) :
        y = x.left                                 
        x.left = y.right                             
        if y.right != self.NULL :
            y.right.parent = x

        y.parent = x.parent                            
        if x.parent == None :                       
            self.root = y                             
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y

    # Fix Insertion
    def fixInsert(self, new_num):
        while new_num.parent.color == 1:                       
            if new_num.parent == new_num.parent.parent.right:       
                u = new_num.parent.parent.left                
                if u.color == 1:                        
                    u.color = 0                        
                    new_num.parent.color = 0
                    new_num.parent.parent.color = 1           
                    new_num = new_num.parent.parent                  
                else:
                    if new_num == new_num.parent.left:               
                        new_num = new_num.parent
                        self.RR(new_num)                        
                    new_num.parent.color = 0
                    new_num.parent.parent.color = 1
                    self.LR(new_num.parent.parent)
            else:                                         
                u = new_num.parent.parent.right                 
                if u.color == 1:                          
                    u.color = 0                           
                    new_num.parent.color = 0
                    new_num.parent.parent.color = 1             
                    new_num = new_num.parent.parent                   
                else:
                    if new_num == new_num.parent.right:               
                        new_num = new_num.parent
                        self.LR(new_num)                        
                    new_num.parent.color = 0
                    new_num.parent.parent.color = 1
                    self.RR(new_num.parent.parent)              
            if new_num == self.root:                            
                break
        self.root.color = 0                               

def search_RB_tree(root, key):
    while root != None and root.val != key:
        if key < root.val:
            root = root.left
        else:
            root = root.right
    if root == None:
        return -1
    return root

def build_RBtree(array):
    RBT = RBTree()
    for num in array:
        RBT.insertNode(num)
    return RBT.root