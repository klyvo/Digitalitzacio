s = input("Di una frase: ")
d = input("Di otra frase: ")

for x in s:
    for y in d:
        if x == y:
            print("Letra en comun: ", x)