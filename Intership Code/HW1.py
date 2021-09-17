#Isha Thukral
# HW1
#Due Date: 02/06/2021, 11:59PM

"""                                   
### Collaboration Statement: Attended office hours 
             
"""


import math
def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    h1 = (perimeter + math.sqrt(perimeter**2 - 16*area)) / 4  # formula to find height of the rectangle
    h2 = (perimeter - math.sqrt(perimeter**2 - 16*area)) / 4  
    h = max(h1, h2) # finding the maximum between both h

    if(float.is_integer(h) == False): # making sure h is int
        return False 

    h = round(h) # rounding h
    w = area / h

    if(float.is_integer(w) == False): #making sure w is int
        return False

    w = round(w) # rounding w
    return max(h, w) # returning the maximum to find longest side of rectangle



def frequency(numList):
    '''
        >>> frequency([3, '7', 5, 5.5, '7', 7, 5.5, 'a', 3, 'a', 'a', 'A'])
        ('a', {3: 2, '7': 2, 5: 1, 5.5: 2, 7: 1, 'a': 3, 'A': 1})
        >>> answer=frequency([6, 5, 7, 7, 7, 5, 5, 5])
        >>> answer[0]
        5
        >>> answer[1]
        {6: 1, 5: 4, 7: 3}
    '''
    #- YOUR CODE STARTS HERE
    x = 0 # list of elements
    organize = {} #open dictionary 
    result = numList[0] # starting of numList 

    for i in numList:
        if i in organize:
            organize[i] += 1 # if frequency increase add one
        else:
            organize[i] = 1 # if only occurs once return 1
    
    for key in organize: # for loop to detect the most frequent item
        if organize[key] > x: # make variable to compare each items frequency
            x = organize[key] # assign x to that item 
            result = key # instead of providing the frequency provide the key that has highest frequency
   
    return result, organize # returning item with highest frequency and follows with remaining items



def successors(file):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    # Open the file and read the contents
    with open(file) as f:   #with ensures the file is properly closed after its suite finishes, even if an error ocurred
        contents = f.read() # use the read() function to read the entire file, contents has the data as string

    #- YOUR CODE STARTS HERE
    open1 = {}
    words = []
    contents = list(contents) 

    for i in range(len(contents)):
        if contents[i].isalnum() != True and contents[i] != " ": # if it is not letter/number/ or space assume punctuation
            contents[i] = ' ' + contents[i] + ' ' #put a space in puncuation

    random = ''.join(contents) # put in together in list but spaced out 
    words = random.split()

    previous = "." # since first element has to be a period 
    for word in words:
        if previous not in open1: # if it its not in dictionary make key
            open1[previous] = [word] # value after the keys
        if word not in open1[previous]:
            open1[previous].append(word) # make new key if its not already one 
        previous = word # change to the element 
    
    
    return open1


def uniqueDigit(num):
    """
        >>> uniqueDigit(123132)
        False
        >>> uniqueDigit(7264578364)
        True
        >>> uniqueDigit(2)
        True
        >>> uniqueDigit(444444)
        False
    """
    #- YOUR CODE STARTS HERE
    digits = []
    max = 0
    
    while num > 0:
        digits.append(num%10) # Begin by separating and storing each number
        if max < num%10: # Then go through each number to find max
            max = num%10 
        num = num// 10
    
    count = 0 # Starting at zero we see how many times max number occurs
    for d in digits:
        if max == d:
            count = count+1 # if the max number is seen more than once then we add +1
    
    if count==1 : # once is allowed as that is the max number 
        return True
    else:    # but if it occurs more than once then we return false
        return False


    
def hailstone(n):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    output = [] # has any empty list for number to append to 
    num = n

    while num != 1: # Uses while loop until num returns to one 
        output.append(num) 
        if (num % 2) == 0: # to check if num is even 
            num = num // 2  # if num even follow this equation 
        else: # if num is odd 
            num = 3 * num + 1 # if num odd follow this equation 
    output.append(num)
        
    return output # returns number in list until it reaches 1 


def common(list1, list2):
    """
        >>> common([12,3,5,8,90,11,44,66,8,9,34,56,-1,0,5,3333,3,2,1],[12,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,44])
        [1, 3, 12, 44]
        >>> common([1,2,3],[4,5,6])
        []

    """
    #- YOUR CODE STARTS HERE
    common = []

    for elements in list1:
        if elements in list2: # see common between two lists
            if elements not in common: # to avoid duplicates check if its already in common
                common.append(elements) # if its not then append to list
    

    return sorted(common) # return in ascending order 

