x1 = int(input("digite um valor....:"))
x2 = int(input("digite outro valor.:"))
x3 = int(input("digite outro valor.:"))
if (x1 != x2 != x3):
    if x1>x2>x3:
        print(x1 , x2 , x3)
    elif x1>x3>x2:
        print(x1 , x3 , x2)
    elif x2>x1>x3:
        print(x2 , x1 , x3)
    elif x2>x3>x1:
        print(x2 , x3 , x1)
    elif x3>x1>x2:
        print(x3 , x1 , x2)
    elif x3>x2>x1:
        print(x3 , x2 , x1)
else:
    print("valores iguais")