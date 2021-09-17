#Lab #5
#Due Date: 03/20/2021, 11:59PM 
# Isha Thukral
'''                                  
# Collaboration Statement: Worked with TA

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.numChildren(x.root)
        2
        >>> x.numChildren(x.root.left)
        2
        >>> x.numChildren(x.root.right)
        1
        >>> x.getMin
        2
        >>> x.getMax
        11
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.isEmpty()
        False
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        # node.left is for less than in binary tree
        # while loop to go through all the lefts till min 
        node = self.root

        while node.left is not None:
            node = node.left
        return node.value

    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE
        # node.right is for greater than in binary tree
        # while loop to go through all the rights till max 
        node = self.root

        while node.right is not None:
            node = node.right
        return node.value

    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        #find this max of left and right and add 1 to get height 
        if node == None:
            return 0
        if node.left == None and node.right == None:
            return 0
        else: 
            max_height = max(self.getHeight(node.left), (self.getHeight(node.right))) +1
            return max_height


    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        # goes through the tree using while loop and comparing 
        current = self.root

        while True:
            if current is None:
                return False
            elif current.value == value:
                return True
            elif value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right

    
    def numChildren(self, node):
        # YOUR CODE STARTS HERE
        # if both than 2
        if node.left is not None and node.right is not None:
            return 2
        elif node.left is not None or node.right is not None:
            return 1 # either or than one 
        else:
            return 0 #else no children 

        


