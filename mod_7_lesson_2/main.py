with open('mysoul.txt', mode='r') as file:
    for l in file:
        if l[0] != '#':
            print(l, end='')
