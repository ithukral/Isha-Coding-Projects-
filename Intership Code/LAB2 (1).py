# LAB2
#Due Date: 02/13/2021, 11:59PM
# Isha Thukral
"""                                   
### Collaboration Statement: worked on with TA
          
"""


class VendingMachine:
    '''
        >>> x=VendingMachine()
        >>> x.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.restock(215, 9)
        'Invalid item'
        >>> x.isStocked
        True
        >>> x.restock(156, 1)
        'Current item stock: 4'
        >>> x.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.purchase(156)
        'Please deposit $1.5'
        >>> x.purchase(156,2)
        'Please deposit $3.0'
        >>> x.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> x.deposit(3)
        'Balance: $3'
        >>> x.purchase(156,3)
        'Please deposit $1.5'
        >>> x.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> x.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.deposit(300)
        'Balance: $300'
        >>> x.purchase(876)
        'Invalid item'
        >>> x.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> x.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> x.purchase(156,3)
        'Please deposit $4.5'
        >>> x.deposit(4.5)
        'Balance: $4.5'
        >>> x.purchase(156,3)
        'Item dispensed'
        >>> x.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> x.purchase(156)
        'Item out of stock'
        >>> x.deposit(6)
        'Balance: $6'
        >>> x.purchase(254,3)
        'Item dispensed'
        >>> x.deposit(9)
        'Balance: $9'
        >>> x.purchase(879,3)
        'Item dispensed'
        >>> x.isStocked
        False
        >>> x.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> x.purchase(156,2)
        'Machine out of stock'
        >>> y=VendingMachine()
        >>> x.setPrice(156, 2.5)
        >>> x.getStock
        {156: [2.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> y.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
    '''

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.vending = { 156: [1.5, 3], 254: [2.0,3], 384: [2.5, 3], 879: [3.0, 3] } #makes vending machine dictionary

        self.balance = 0 # sets vending machine balance equal to 0


    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        
        if not self.isStocked:
            return 'Machine out of stock' # if there is no stock return this function 
        elif item in self.vending: # if it is continue 
            total = qty * self.vending[item][0] # how much needs to be payed 
            if self.vending[item][1] == 0: # if a specific item is not stocked 
                return 'Item out of stock' # return this function
            if qty <= self.vending[item][1]: # if enough stock of the item continue 
                if self.balance < total: 
                    remaining = total - self.balance # if not enough has been inputed find the remaining
                    return 'Please deposit ${0}'.format(remaining) # ask for the remaining 
                self.vending[item][1] -= qty # updating the stock in vending machine 
                remaining = self.balance - total # and the balance
                self.balance = 0 # for next customer balance must be re adjusted again
                if remaining == 0: # perfect amount has been inputed
                        return 'Item dispensed'
                else:
                    return 'Item dispensed, take your ${0} back'.format(remaining) # if change needs to be given
            else:
                return 'Current {} stock: {}, try again'.format(item, self.vending[item][1]) # if specific item is not enough for quantity
      
        else: 
            return 'Invalid item'


    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        if self.isStocked: # if item is stocked 
            self.balance += amount # updates the balance 
            return "Balance: ${0}".format(self.balance) 
        else:
            return 'Machine out of stock. Take your ${0} back'.format(amount)
 

    def restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        if item in self.vending:  
            self.vending[item][1] += stock # adding stocks of specific item 
            return 'Current item stock: {}'.format(self.vending[item][1]) # and update of stock 
        else:
            return 'Invalid item'
    

    @property
    def isStocked(self):
        #--- YOUR CODE STARTS HERE
        for item in  self.vending.values():        
            if item[1] > 0: # to check if there is stock of the item 
                return True

        return False
    

    @property
    def getStock(self):
        #--- YOUR CODE STARTS HERE
        return self.vending  # return the dictionary 



    def setPrice(self, item, new_price):
        #--- YOUR CODE STARTS HERE
        if item in self.vending:
            self.vending[item][0] = new_price # updates the price of the item 
        else:
            return 'Invalid item'


## Section 2
class Complex:
    '''
        >>> a=Complex(5.2,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7.2, 8i)
        >>> a-b
        (3.2, -20i)
        >>> a*b
        (94.4, 60.8i)
        >>> a/b
        (-0.368, -0.424i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> 5+a
        (10.2, -6i)
        >>> a+5
        (10.2, -6i)
        >>> 5-b
        (3, -14i)
        >>> b-5
        (-3, 14i)
        >>> print(a)
        5.2-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> a.conjugate
        (5.2, 6i)
        >>> b.conjugate
        (2, -14i)
        >>> isinstance(b.conjugate, Complex)
        True
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
        >>> a==9.5
        False
    '''

    # - DO NOT MODIFY THE CONSTRUCTOR
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def conjugate(self):
        #--- YOUR CODE STARTS HERE
        return Complex(self.real, -self.imag) #-num = -1*num 
    
    def __str__(self):
        if self.real == 0: 
            return "{}i".format( self.imag) # return without the self.real
        if self.imag == 0:
            return "{}".format(self.real) # returns without the self.imag
        if self.imag > 0:
            return "{}+{}i".format(self.real, self.imag) # includes if self.imag is not negatice 
        return "{}{}i".format(self.real, self.imag) # if both exist then it return both
        
    def __repr__(self):
        return "({}, {}i)".format(self.real, self.imag) # return the elements with the complex format

    def __eq__(self, other):
        if type(other) == Complex: # checks to make sure it element is complex
            if other.real == self.real and other.imag == self.imag:  # making sure that they match same format
                return True
            else:
                return False 
        return False

    def __add__(self, other):
        if type(other) == Complex and type(self) == Complex: # checking its type 
            addition_real = (self.real + other.real) # adding 
            addition_imag = (self.imag + other.imag)
        elif type(other) != Complex and type(self) == Complex:
            addition_real = (self.real + other.real) # if other is not complex 
            addition_imag = (self.imag)
        else:
            addition_real = (self.real + other.real)
            addition_imag = (other.imag) # if self not complex 
        return Complex(addition_real, addition_imag)

    def __radd__(self,other):
        return self+other # TA explained this function includes the reverse 

    def __sub__(self, other):
        if type(other) == Complex and type(self) == Complex:
            sub_real = (self.real - other.real) # subtracting 
            sub_imag = (self.imag - other.imag)
        elif type(other) != Complex and type(self) == Complex:
            sub_real = (self.real - other.real) # if other is not complex 
            sub_imag = (self.imag)
        else:
            sub_real = (self.real - other.real)
            sub_imag = (other.imag) # if self not complex 
        return Complex(sub_real, sub_imag) # add complex to make sure it returns with i for imag

    def __rsub__(self, other):
        return Complex(-self.real,-self.imag) + other # makes sure that it returns with correct + or negative sign due to subtraction 

    def __mul__(self, other):
        if type(other) == Complex and type(self) == Complex:
            mul_real = (self.real*other.real - self.imag*other.imag) # multiplication 
            mul_imag = (self.real*other.imag + self.imag*other.real)
        elif type(other) != Complex and type(self) == Complex:
            mul_real = (self.real*other.real)
            mul_imag = (self.imag*other.real) # if other not complex
        else:
            mul_real = (self.real*other.real) # if self not complex
            mul_imag = (self.real*other.imag)
        return Complex(mul_real, mul_imag)

    def __rmul__(self, other):
        return  self*other

    def __truediv__(self, other):
        div_real = (self.real*other.real + self.imag*other.imag)/(other.real*other.real+ other.imag*other.imag) # only true division 
        div_imag = (self.imag*other.real - self.real*other.imag )/(other.real*other.real+ other.imag*other.imag) # plug int using formula provided in instruction
        return Complex(div_real, div_imag) # because of the division function we dont use rdiv
