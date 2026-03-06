n = int(input("digite um número inteiro e positivo..:"))
x = 1
if n > 0:
    print("S =", end="")
    while x <= n:
        print(f" 1/{x} ", end="")
        x = x + 1
        if x <= n:
            print("+", end="")
elif n == float:
    print("valor decimal")
else:
    print("valor não inteiro ou negativo")