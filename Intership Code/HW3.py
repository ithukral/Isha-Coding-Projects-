# HW3
#Due Date: 03/13/2021, 11:59PM
# Isha Thukral

"""                                   
### Collaboration Statement: Worked with TA (Chandu and Timothy)
             
"""

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

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


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        # strip removes spaces 
        # txt within float checks the string

        try: 
            float(txt.strip()) 
            return True
        except ValueError:
            return False
    
    def operation_check(self,alist):
        # checking for operation
        operations = ['+','-','/','*','^']

        for i in range(len(alist)-1):
            if alist[i] in operations:
                if alist[i+1] in operations:
                    return False
            
            if alist[i] == ')':
                if alist[i+1] == '(':
                    return False
        return True

    def number_check(self,alist):
        # if it is not an operation we assume its a number 
        operations = ['+','-','/','*','^',')','(']

        for i in range(len(alist)-1):
            if not alist[i] in operations:
                if not alist[i+1] in operations[:-1]:
                    return False
        return True

    def isbalanced(self,alist):
        #checks if the open and closed parenthesis are balanced
        count = 0

        for op in alist:
            if op == '(':
                count += 1
            elif op == ')':
                count -= 1

            if count < 0:
                return False
        
        if count ==0 :
            return True
        else:
            return False


    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5 % + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        txt = txt.strip()
        items = txt.split()
        items = self.addstars(items)
        oprcheck = self.operation_check(items)
        numcheck = self.number_check(items)
        balanced = self.isbalanced(items)

        if not oprcheck:
            return
        if not numcheck:
            return
        if not balanced:
            return
        if len(items) == 0:
            return
        elif len(items) == 1:
            if self._isNumber(items[0]):
                return str(float(items[0]))
            else:
                return
        elif items[0] in '+-/*)' or items[-1] in '+-/*(' :
            return
        else:
            pStack = Stack()  # method must use postfixStack to compute the postfix expression
            ans = []
            prec = {'+': 1, '-':1, '*':2 , '/':2 , '^':3, '(': 0, ')':0}
            for op in items:
                if(op == ' '):
                    continue
                if self._isNumber(op):
                    ans.append(str(float(op))) #  output must be represented as a float
                else:
                    if op == '(':
                        pStack.push(op)
                    elif op == ')':
                        while(not pStack.isEmpty() and pStack.peek() != '('):
                            ans.append(pStack.peek())
                            pStack.pop()
                        if(not pStack.isEmpty()):
                            # removing the (
                            pStack.pop()
                    else:
                        # + - * / ^
                        while(not pStack.isEmpty() and not prec[op] > prec[pStack.peek()]):
                            top = pStack.peek()
                            if top == '(': # when closing ')'  put operation on list 
                                break
                            if op == '^' and pStack.peek() == '^':
                                break
                            else:
                                ans.append(top)
                                pStack.pop()
                        
                        pStack.push(op)

            while (not pStack.isEmpty()):
                ans.append(pStack.peek())
                pStack.pop()

        return ' '.join(ans)

    def addstars(self,alist):
        modified_list = []
        # 2() -> 2*()
        #()() -> ()*()
        for i in range(len(alist)-1):
            if self._isNumber(alist[i]) and alist[i+1] == '(':
                modified_list.append(alist[i])
                modified_list.append('*')
            elif alist[i] == ')' and alist[i+1] == '(':
                modified_list.append(alist[i])
                modified_list.append('*')
            else:
                modified_list.append(alist[i])
        modified_list.append(alist[-1])
        return modified_list

    def exeOpr(self,operand1,operand2,operation):
        # if the operation equals operation perform that operation 
        if operation == '+':
            return float(operand1) + float(operand2)
        elif operation == '-':
            return float(operand1) - float(operand2)
        elif operation == '*':
            return float(operand1) * float(operand2)
        elif operation == '/':
            return float(operand1) / float(operand2)
        else:
            return float(operand1) ** float(operand2)

    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate

            # For extra credit only. If not attemped, these cases must return None
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
            46.666666666666664
        '''
        # YOUR CODE STARTS HERE

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        postfix = self._getPostfix(self.__expr)
        
        if postfix is None:
            return
        items = postfix.split()
        if items is []:
            return 
        for item in items:
            if self._isNumber(item):
                calcStack.push(item)
            else:
                # item is an operation
                operand2 = calcStack.pop()
                operand1 = calcStack.pop()
                result = self.exeOpr(operand1,operand2,item)
            
                calcStack.push(result)
        
        return calcStack.pop()


#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if type(word) is str:
            if word.isalnum() and word[0].isalpha():
                return True
            else:
                return False
        else:
            return False
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        variable = expr.split()
        
        # finding the variable and replace with the matching _isVariable
        for i in range(len(variable)):
            if self._isVariable(variable[i]):
                if variable[i] in self.states:
                    variable[i] = str(self.states[variable[i]]) # convert to string 
                else:
                    return None
                    
        return ' '.join(variable)

    
    def calculateExpressions(self):
        self.states = {}
        lines = self.expressions.split(';')
        return_smt = lines.pop().split('return')[1].strip()
        calcObj = Calculator()     # method must use calcObj to compute each expression

        # YOUR CODE STARTS HERE
        steps = {}
        
        # split if =  and strip left and right using [index#]
        for line in lines:
            both = line.split('=')
            left = both[0].strip()
            right = both[1].strip()

            right = self._replaceVariables(right) # 1+9 doctest example 

            if right is None:
                self.states = {}
                return None

            calcObj.setExpr(right)
            self.states[left] = float(calcObj.calculate)#10

            steps[line] = self.states.copy()

        return_smt = self._replaceVariables(return_smt)
        if right is None:
            self.states = {}
            return None
        
        calcObj.setExpr(return_smt)
        steps['_return_'] = float(calcObj.calculate)

        return steps
