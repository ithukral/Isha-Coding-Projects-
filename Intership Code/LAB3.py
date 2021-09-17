# LAB3
#Due Date: 02/27/2021, 11:59PM
# Isha Thukral
"""                                   
### Collaboration Statement: Worked with TA
             
"""

#REMINDER: All functions should NOT contain any for/while loops or global variables. 
#          Use recursion, otherwise no credit will be given


def lineUp(aList1, aList2):
    '''
        >>> lineUp([5, 8.9, 'a'], [6, 5, 4, 21, -9, 's', 8.9, 45, 1, 1, 'a', 3])
        True
        >>> lineUp([5, 8.9, 'a'], [6, 5, 4, 21, -9, 'a', 8.9, 45, 1, 1, 3])
        False
        >>> lineUp([5, 8.9, 'a'], [6, 5, 4, 21, -9, 'a', 45, 1, 1, 3])
        False
        >>> lineUp([2, -6, 5, 3], [6, 1, 0, 2, -6, 4, 12, 5, 2, 3])
        True
    '''
    ## YOUR CODE STARTS HERE
    if len(aList1) == 0: # base case for True 
        return True
    if len(aList2) == 0: # base case for False
        return False
    if aList1[0] == aList2[0]: #seeing if the elements match 
        return lineUp(aList1[1:], aList2[1:]) # if they do go to next index's
    else:
        return lineUp(aList1, aList2[1:]) # if not than try to find the match


def removing(aList):
    """
    >>> removing([7, 4, 0])
    [7, 4, 0]
    >>> myList=[7, 4, -2, 1, 9]
    >>> removing(myList)   # Found(-2) Delete -2 and 1
    [7, 4, 9]
    >>> myList
    [7, 4, -2, 1, 9]
    >>> removing([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
    [9]
    >>> removing([-3, -4, 5, -4, 1])  # Found(-3) Delete -2, -4 and 5. Found(-4) Delete -4 and 1
    []
    """
    ## YOUR CODE STARTS HERE
    if aList == []: # when the list is empty
        return []
    if aList[0] >= 0:
        return [aList[0]] + removing(aList[1:]) # adds the rest of the list as index 0 was positive
    elif aList[0] < 0: # if the element isn't positive
        absolute = aList[0] * -1 # absolute value 
        return removing(aList[absolute:]) # returns the elements after the negative number and the next x-1elements,  
        

def neighbor(n):
    """
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    """
    ## YOUR CODE STARTS HERE
    # n(678) -> n(67)*10+8 -> (6*10 +7)*10+8 = 678
    # 678//10 -> 67
    # n(6777) -> n(677) -> n(67) -> (6*10 +7) = 67
    if n < 10: # if less than 10 can't compare to anything 
        return n
    if n%10 == (n//10)%10 : # if the last two digits equal 
        return neighbor(n//10) # returning one on the int 
    else:
        return neighbor(n//10)*10 + n%10

