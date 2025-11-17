list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
for x in list_num:
    for y in list_num:
        if x == y:
            list_num.remove()
print(list_num)