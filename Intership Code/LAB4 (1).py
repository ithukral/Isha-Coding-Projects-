# LAB4
#Due Date: 03/06/2021, 11:59PM
# Isha Thukral

"""                                   
### Collaboration Statement: Worked on with TA (Vivek and Chandu)
             
"""

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.replicate()
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 4 -> 5 -> 5 -> 5 -> 5 -> 5 -> 8.76 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return 'Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out)

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        new_node = Node(value)
        # if the list is empty add value to head
        if self.isEmpty():
            self.head = new_node 
            self.tail = new_node
        else:
            if new_node.value <= self.head.value: # add at start
                new_node.next = self.head # linking new_node to head
                self.head = new_node # updating the position of the head
            elif new_node.value >= self.tail.value:
                self.tail.next = new_node # linking tail to new node
                self.tail = new_node # updating the position of the tail
            else:
                current = self.head
                x = None # the x will be one behind current 
                while(current.value < new_node.value): # ascending order
                    x = current 
                    current = current.next # going to next value within link list 
                x.next = new_node # placing after next value 
                new_node.next = current # placing before next value 


    def replicate(self):
        # --- YOUR CODE STARTS HERE
        new_sorted = SortedLinkedList() # creates sorted linked list
        sorted_head = self.head # value to be evaluated

        while sorted_head != None: 
            if sorted_head.value <= 0: # if negative or adding one zero
                new_sorted.add(sorted_head.value) # add without duplicating
            elif isinstance(sorted_head.value, int): # if the value is an integer
                for i in range(sorted_head.value): # for loop to see how many times replicate value
                    new_sorted.add(sorted_head.value)
            else:
                new_sorted.add(sorted_head.value) # if anything apart from other value types add once
            sorted_head = sorted_head.next
        return new_sorted # returning the linked list


    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        if self.isEmpty(): # if the link list is empty return None
            return None
        sorted_head = self.head

        while sorted_head.next != None: # loop until None is element
            if sorted_head.value == sorted_head.next.value: # if the value is the same
                sorted_head.next = sorted_head.next.next # in linked list we use pointer to redirect rather than remove
                if sorted_head.next == None: # when approaches end of linked list None will be returned
                    self.tail = sorted_head # Hence we make sorted_head the tail
            else:
                sorted_head = sorted_head.next # if not equal go to the next value


