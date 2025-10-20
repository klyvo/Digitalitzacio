a = input("Di un numero: ")
if(a.isnumeric()):
    print("n es numeric")
    reste = int(a)%2
    if reste == 0:
        print("Aquest numero es parell.")
    else:
        print("Aquest numero es parell")
