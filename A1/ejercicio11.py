s = input("Di una palabra: ")
letra = input("Di la letra que vols comptar: ")
contador = 0
for x in s:
    if x == letra:
        contador += 1
        if contador > 0:
            print("La lletra ", letra, " apareix ", contador, " vegades")
        elif contador == 0:
            print("La lletra ", letra, " no apareix")