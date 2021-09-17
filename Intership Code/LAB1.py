#Isha Thukral
#Lab #1
#Due Date: 01/30/2021, 11:59PM

"""                                   
    Collaboration Statement: Worked on during office hour.
             
"""

def lowerFactorial(x, n):
    """
        >>> lowerFactorial(4, 2)
        12
        >>> lowerFactorial(34, 3)
        35904
        >>> lowerFactorial(0, 45)
        >>> lowerFactorial(4, -2) is None
        True
        >>> lowerFactorial(5.67, 4)   
    """
    # - YOUR CODE STARTS HERE -
    if (type(x) == int) and (type(n) == int):
        if x> 0 and n>= 0:
            i = 0
            fact = 1
            while i < n:
                fact = fact * (x-i)
                i += 1
            return fact
    else: 
        return(None)


    