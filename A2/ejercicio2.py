list_num = [2, 7, 4, 4, 4, 8, 3, 9, 6, 10]
print(list_num)
a = int(input("Qué numero quieres contar: "))
contador = 0
for x in list_num:
    if x == a:
        contador+=1

print("Ese numero aparece", contador, "veces")