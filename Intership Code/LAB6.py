#Lab #6
#Due Date: 03/27/2021, 11:59PM 
# Isha Thukral
'''                                 
# Collaboration Statement: Worked with TA (Chandu)

'''


class MinPriorityQueue:
    '''
        >>> h = MinPriorityQueue()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        # YOUR CODE STARTS HERE
        return len(self._heap)

    @property
    def getMin(self):
        # YOUR CODE STARTS HERE
        # this is a min binary heap
        return self._heap[0]
    
    
    def _parent(self,index):
        # YOUR CODE STARTS HERE
        # by using floor division and subracting by 1 (because heap starts at 1 while list index starts at 0)
        if index <= 1 or index> len(self._heap):
            return None
        return self._heap[(index//2)-1]

    def _leftChild(self,index):
        # YOUR CODE STARTS HERE
        # -1 as we go left to right for heaps in the list
        left = (2 * index) -1

        if left >= len(self._heap) or left <= 0:
            return None
        else:
            return self._heap[left]



    def _rightChild(self,index):
        # YOUR CODE STARTS HERE
        # same for right except the -1 gets cancelled out
        right = (2 * index)

        if right >= len(self._heap) or right <= 1:
            return None
        else:
            return self._heap[right]

    def insert(self,item):
        # YOUR CODE STARTS HERE
        self._heap.append(item)
        index = len(self._heap)

        # when the child is less than parent swap till it isn't 
        # making the child equal to the parent
        while self._parent(index)!= None and self._parent(index) > item:
            self._heap[index -1] = self._heap[(index//2)-1]
            self._heap[(index//2)-1] = item
            index = index//2

            

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            x=self._heap[0]
            self._heap=[]
            return x
        else:
            # YOUR CODE STARTS HERE
            # we remove the min which is the root node
            oldmin = self._heap[0]
            self._heap[0] = self._heap[-1]
            self._heap.pop()
            parent = self._heap[0]
            index = 1
            # conditions to make sure that min binary tree follows the numerical order 
            while self._leftChild(index) != None:
                if self._rightChild(index) != None:
                    if min(self._leftChild(index),self._rightChild(index)) >= parent:
                        break
                    else:
                        # if right greater than left shift left up
                        if self._rightChild(index) > self._leftChild(index):
                            self._heap[index-1] = self._heap[2*index-1]
                            self._heap[2*index-1] = parent
                            index = 2*index
                        else:
                        # if left greater than right
                            self._heap[index-1] = self._heap[2*index]
                            self._heap[2*index] = parent
                            index = 2*index+1
                else:
                    if self._leftChild(index) >= parent:
                        break
                    else:
                        self._heap[index-1] = self._heap[2*index-1]
                        self._heap[2*index-1] = parent
                        index = 2*index
            return oldmin
