#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

#has_33([1, 3, 3]) → True
#has_33([1, 3, 1, 3]) → False
#has_33([3, 1, 3]) → False

def has_33(nums):
    last = nums[0]

    for num in nums[1:]:
        if num == last: 
            return True
        last=num # to check the last val and the num to be equal
    return False

print(has_33([3,1,2,3]))