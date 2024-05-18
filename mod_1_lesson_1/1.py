"""«Часть от целого»."""

inn = input()
new_lst = [i for i in inn]
for i in new_lst:
    if i == ".":
        print(inn[1:new_lst.index(i)+1])
        break
