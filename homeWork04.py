x = 0
immutable_var = (1, "string", True, x, 1.5, [7, 8])
print(immutable_var)
#immutable_var[0] = 2 - нельзя изменить элементы, входящие в кортеж. Но можно изменить значения вложенного списка
immutable_var[-1][0] = 99
print(immutable_var)
multable_list = ["list", 12, 3.7, False, x]
multable_list[1] = 21
print(multable_list)