#map() = map(function,iterables)
################################

my_num = [2,3,4,5,6,7,8]
def square(nums):
    return nums**2

print(list(map(square,my_num)))
######################################

#lambda arguments:expression

lambda nums: nums**2

print(list(map(lambda nums: nums**2,my_num)))


######################################
#filter() = filter(fucntion,iterables)

my_num = [2,3,4,5,6,7,8]

def even_num(nums):
    return nums%2==0

print(list(filter(even_num,my_num)))

######################################
#lambda

lambda nums: nums%2==0

print(list(filter(lambda nums: nums%2==0,my_num)))
