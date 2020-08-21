#Animal Crackers: Write a function that takes a two-word string and returns True if both words begin with same letter.

#Output
#animal_crackers("Levelheaded Llama") --> True
#animal_crackers("Crazy Kangaroo") --> False

# Solution 1
def animal_crackers(text):
    
    wordlist=text.split() # can also be done with text.lower().split()
    first = wordlist[0].lower()
    second = wordlist[1].lower()

    if list(first[0]) == list(second[0]):
        return True
    else:
        return False
print(animal_crackers("Awesome alligator"))
print(animal_crackers("Awesome Perumal"))

#Solution 2

def animal_crackers(text):
    
    wordlist=text.split()
    first = wordlist[0].lower()
    second = wordlist[1].lower()

    return first[0] == second[0]

print(animal_crackers("Awesome alligator"))
print(animal_crackers("Awesome Perumal"))


# Solution 3 

def animal_crackers(text):
    
    wordlist=text.split()

    return wordlist[0][0] == wordlist[1][0]


print(animal_crackers("Kanje Kabothi"))
print(animal_crackers("Shama Nathari"))



