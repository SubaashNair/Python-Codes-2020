#lesser of two evens(2,4) ---> 2
#lesser of two evens(2,5) ---> 5


#solution 1

def lesser_of_two_evens(a,b):
    new_str = [a,b]
    if a % 2== 0 and b % 2 ==0:
        #both numbers are even
        return min(new_str)
        #return the min value which is added in new_str
    else:
        return max(new_str)
        #return the max value which is added in new_str

print(lesser_of_two_evens(2,4))


#Solution 2

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        result = min(a,b)
    else:
        result = max(a,b)
    return result

print(lesser_of_two_evens(2,5))

#Solution 3

def lesser_of_two_evens(a,b):
    if a % 2 == 0  and b % 2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result

print(lesser_of_two_evens(3,5))