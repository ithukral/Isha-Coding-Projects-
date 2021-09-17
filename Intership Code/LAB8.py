#Lab #8
#Due Date: 04/24/2021, 11:59PM 
# Isha Thukral
'''                                 
# Collaboration Statement:  Worked with TA (Chandu)

'''

def mulDigits(num, fn):
    '''
        >>> isTwo = lambda num: num == 2
        >>> mulDigits(5724892472, isTwo)
        8
        >>> def divByFour(num):
        ...     return not num%4
        ...
        >>> mulDigits(5724892472, divByFour)
        128
        >>> mulDigits(155794, isTwo)
        1
        >>> mulDigits(67945125482222152, isTwo)
        64
        >>> mulDigits(679451254828822152, divByFour)
        8192
    '''
    # YOUR CODE STARTS HERE
    ans = 1
    while num > 0:
        dig = num % 10 
        if fn(dig):
            ans *= dig # multipy the digit if its either same int or divisible by 
        num //= 10 # so we can move on to the next element
    return ans # returns the multiplied num




def getCount(x):
    '''
        >>> getCount(6)(62156)
        2
        >>> digit = getCount(7)
        >>> digit(9457845778457077076)
        7
        >>> digit(-945784578457077076)
        6
        >>> getCount(6)(-65062156)
        3
    '''
    # YOUR CODE STARTS HERE
    def fn(n): # can't do by list hence using fn 
        if n <0:
            n = -n
        count = 0 
        while n >0: # while there are still elements
            dig = n%10 # takes the last element 
            if dig == x: # comes to x 
                count += 1 # iterate  one and more 
            n//=10 # floor division by 10 
        return count

    return fn # because we have done it as a function within we must return 
    
# getNumber(5)([1,3,4,6])

def getNumber(num):

    def fn(lst):
        lst = sorted(lst)
        dif = num
        ans = 0
        for i in lst:
            # num -> 5, i -> 6
            # num-i -> -1
            if(dif >= num-i):
                dif = num -i
                if(dif >=0 ):
                    ans = i
                else:
                    break
        return ans
    return fn

# >>> def genForever(lst):
# ...     i = 0
# ...     while True:
# ...             yield lst[i]
# ...             i+=1
# ...             if i==len(lst):
# ...                     i=0







def genAccum(seq, fn):
    '''
        >>> add = lambda x, y: x + y
        >>> mul = lambda x, y: x * y
        >>> type(genAccum([7, 2, 3, 4, 5, 6, 7, 8, 9, 10], add)) 
        <class 'generator'>
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
        >>> list(genAccum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
        >>> list(genAccum([7, 2, 3, 4, 5, 6, 7, 8, 9, 10], add))
        [7, 9, 12, 16, 21, 27, 34, 42, 51, 61]
        >>> list(genAccum([2.5, 2, 3, 4, 5, 0, 7, 8, 9, 10], mul)) 
        [2.5, 5.0, 15.0, 60.0, 300.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        >>> list(genAccum([0, 2, 3, 4, 5, 6, 7, 8, 9, 10], mul))
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> list(genAccum([1, 2, 3, 4, 5, 0, 7, 8, 9, 10], mul))
        [1, 2, 6, 24, 120, 0, 0, 0, 0, 0]
    '''
    # YOUR CODE STARTS HERE
    gen = iter(seq)
    n = next(gen)
    yield n

    while True: # an alternate way without inter: for i in gen:
        i = next(gen, None) # n = fn(n, i)
        if i != None: # n = seq[0]
            n = fn(n,i)
            yield n
        else:
            break
    # for i in range(1, len(seq)):
    #     n = fn(n,seq[i])
    #     yield n


    
    
