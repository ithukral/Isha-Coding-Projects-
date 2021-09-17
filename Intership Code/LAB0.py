#Isha Thukral
#Lab #0
#Due Date: 01/22/2021, 11:59PM
"""                                   
### Collaboration Statement: Attended office hours 
             
"""

# More information on pass statement: https://docs.python.org/3/reference/simple_stmts.html#the-pass-statement

def sumSquares(aList):
   # """
    #   >>> sumSquares(5)
    #     >>> sumSquares('5') is None
    #    True
    #    >>> sumSquares(6.15)
    #    >>> sumSquares([1,5,-3,5,9,8,14,-25])
    #    277
    #    >>> sumSquares(['14',5,-3,5,9.0,8,14,7,'Hello'])
    #    245
        
   # """
    # --- YOU CODE STARTS HERE
    total = 0
    if type(aList) == list:
        for x in aList: 
            if (type(x) == int) and x > 0:
                if x % 3 == 0 or x % 7 == 0:
                    total += x**2
        return total
    else:
        return(None)     


