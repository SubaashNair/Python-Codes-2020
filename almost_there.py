
#almost_there(90) --> True
#almost_there(104) --> True
#almost_there(150) --> False
#almost_there(209) --> True

#Given an integer n, return True if n is within 10 of either 100 or 200

import math
def almost_there(n):
    if n >= 90 and n <= 105:
        return True
    elif n>=190 and n<=209:
        return True
    else:
        return False
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))