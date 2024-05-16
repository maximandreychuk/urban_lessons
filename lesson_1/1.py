"""«Часть от целого»."""

inn = input()
lst = [i for i in inn]
for i in lst:
    if i == ".":
        print(inn[1:lst.index(i)+1])
        break