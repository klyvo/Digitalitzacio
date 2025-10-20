a = int(input("Di un numero: "))
b = int(input("Di otro numero: "))
c = int(input("Di un ultimo numero: "))

if a > b and a > c:
    print(a, "es el mayor")
elif b > a and b > c:
    print(b, "es el mayor") 
else:
    print(c, "es el mayor")