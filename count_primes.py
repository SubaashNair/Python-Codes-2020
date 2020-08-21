#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#count_primes(100) --> 25
#By convention, 0 and 1 are not prime.

def count_primes(num):

    count = 0 
    num_val = 0

    for val in range(0,num+1):
        if val % 1 == 0 and val % val == 0:
            count+=1
            num_val+=val
        elif val == 0 and val == 1:
            count+=1
        return num_val
print(count_primes(100))
        