#Lab #7
#Due Date: 04/10/2021, 11:59PM 
# Isha Thukral
'''                                 
# Collaboration Statement: Worked with TA (Chandu)

'''


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
# ============================= COPY/PASTE your Stack class from HW3 HERE =================================  
class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return True
        else:
            return False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        count = self.top
        number = 0
        while count is not None:
            count = count.next
            number += 1
        return number

    def push(self,value):
        # YOUR CODE STARTS HERE
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node
     
    def pop(self):
        # YOUR CODE STARTS HERE
        if (self.isEmpty() == False):
            value = self.top.value
            self.top = self.top.next
            return value
        

    def peek(self):
        # YOUR CODE STARTS HERE
        if (self.isEmpty() == False):
            return self.top.value

# ============================= Section 1 =================================                         
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> len(x)
        2
        >>> x
        Head:Node(2)
        Tail:Node(3)
        Queue:2 -> 3
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        self.count = 0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.head == None:
            return True
        else:
            return False
        
    def enqueue(self, value):
        # YOUR CODE STARTS HERE
        new = Node(value)

        if self.isEmpty() == True:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new # making the new node the new tail
            self.tail = new 
        self.count = self.count + 1 # adding that count 

     
    def dequeue(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return None
        out = self.head.value
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next # making the new head the node next to the current head
        self.count -= 1 
        return out 
        

    def __len__(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() == True:
            return 0
        else:
            return self.count 


# ============================= Section 2 =================================
class Graph:
    def __init__(self, graph_repr):
        self.vertList = graph_repr


    def bfs(self, start):
        '''
            Method uses an instance of the Queue class to process nodes

            >>> g3 = {'B': [('E', 3), ('C', 5)],
            ...       'F': [],
            ...       'C': [('F', 2)],
            ...       'A': [('D', 3), ('B', 2)],
            ...       'D': [('C', 1)],
            ...       'E': [('F', 4)]}
            >>> g = Graph(g3)
            >>> g.bfs('A')
            ['A', 'B', 'D', 'C', 'E', 'F']

            >>> g4 = {'Bran': ['East', 'Cap'],
            ...       'Flor': [],
            ...       'Cap':  ['Flor'],
            ...       'Apr':  ['Dec', 'Bran'],
            ...       'Dec':  ['Cap'],
            ...       'East': ['Flor']}
            >>> g = Graph(g4)
            >>> g.bfs('Apr')
            ['Apr', 'Bran', 'Dec', 'Cap', 'East', 'Flor']
        '''
        # YOUR CODE STARTS HERE
        bfsQ = Queue()
        seen = []
        bfsQ.enqueue(start)
        seen.append(start)

        while bfsQ.isEmpty() == False:
            element = bfsQ.dequeue()
            for  i in sorted(self.vertList[element]): # sorted make sure in alphabetical order when comparing 
                if isinstance(i,tuple): # checking if i is a tuple 
                    i = i[0]
                if i not in seen: # to make sure not repeats 
                    bfsQ.enqueue(i)
                    seen.append(i)
        return seen



    def dfs(self, start):
        '''
            Method uses an instance of the Stack class to process nodes

            >>> g3 = {'B': [('E', 3), ('C', 5)],
            ...       'F': [],
            ...       'C': [('F', 2)],
            ...       'A': [('D', 3), ('B', 2)],
            ...       'D': [('C', 1)],
            ...       'E': [('F', 4)]}
            >>> g = Graph(g3)
            >>> g.dfs('A')
            ['A', 'B', 'C', 'F', 'E', 'D']

            >>> g4 = {'Bran': ['East', 'Cap'],
            ...       'Flor': [],
            ...       'Cap':  ['Flor'],
            ...       'Apr':  ['Dec', 'Bran'],
            ...       'Dec':  ['Cap'],
            ...       'East': ['Flor']}
            >>> g = Graph(g4)
            >>> g.dfs('Apr')
            ['Apr', 'Bran', 'Cap', 'Flor', 'East', 'Dec']
        '''
        # YOUR CODE STARTS HERE
        dfsS = Stack()
        seen = []
        dfsS.push(start)

        while dfsS.isEmpty() == False: # dfs we traverse down before going to the next element 
            element = dfsS.pop()
            if element not in seen: # if it is not already been visited and appended
                seen.append(element)
            neighbours = sorted(self.vertList[element])
            neighbours.reverse() # reversing vertList
            for  i in neighbours:
                if isinstance(i,tuple):
                    i = i[0]
                if i not in seen:
                    dfsS.push(i)
        return seen






# ---------------- EXTRA CREDIT -------------- #
def selectionSort(numList):
    '''
        >>> x=[9,3,5,4,1,67,78]
        >>> selectionSort(x)
        {1: [9, 3, 5, 4, 1, 67, 78], 2: [1, 3, 5, 4, 9, 67, 78], 3: [1, 3, 5, 4, 9, 67, 78], 4: [1, 3, 4, 5, 9, 67, 78], 5: [1, 3, 4, 5, 9, 67, 78], 6: [1, 3, 4, 5, 9, 67, 78], 7: [1, 3, 4, 5, 9, 67, 78]}
        >>> x
        [1, 3, 4, 5, 9, 67, 78]
        >>> selectionSort([4, 1, 33, -7, -98, 2])
        {1: [4, 1, 33, -7, -98, 2], 2: [-98, 1, 33, -7, 4, 2], 3: [-98, -7, 33, 1, 4, 2], 4: [-98, -7, 1, 33, 4, 2], 5: [-98, -7, 1, 2, 4, 33], 6: [-98, -7, 1, 2, 4, 33]}
    '''
    # YOUR CODE STARTS HERE
    #numList = sorted(numList) The comments bellow are a dry run of the doctest
    seen = {}
    len_1 = len(numList)

    for i in range(len_1):
        min_i = i #0
        seen[i + 1] = numList.copy()
        for j in range(i+1,len_1): #1-> len i
            if numList[min_i] > numList[j]: #numList[min_i] 3  < 1
                min_i = j  # min_i = 4
        temp = numList[min_i]
        numList[min_i] = numList[i] # switching order of numList[min_i], numList[i]
        numList[i] = temp
    return seen