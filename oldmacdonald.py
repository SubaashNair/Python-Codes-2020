#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

#old_macdonald('macdonald') ---> MacDonald

def old_macdonald(name):
    first = name[:3]
    last = name[3:]

    return first.capitalize() + last.capitalize()


print(old_macdonald("macdonald"))