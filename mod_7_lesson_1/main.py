from pprint import pprint


file = open('mysoul.txt', 'r')
file_content = file.read()
file.close()
pprint(file_content)
