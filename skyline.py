#Skyline 

#input('Anthropromorphism')
#output('aNtHrOpOmOrPhIsM')

def myfunc(*args):
    new_list = ''
    a_list = list(*args)

    for index, alph in enumerate(a_list):
        if index %2 == 0:
            new_list+=alph.upper()
        else:
            new_list+=alph
    return new_list

print(myfunc('Anthropromorphism'))