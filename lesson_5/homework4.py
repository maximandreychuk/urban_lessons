immutable_var = ([1,2], True, "foodBar")
print("Кортеж: ",immutable_var)

try:
    immutable_var[1] = True
except TypeError:
    print("Кортеж является неизменяемым типом данных.")


mutable_list = [1,4,2,13,False, "Barfood"]
print("Cписок: ", mutable_list)
mutable_list[4], mutable_list[5] = True, "jdm"
print("Измененный список: ", mutable_list)