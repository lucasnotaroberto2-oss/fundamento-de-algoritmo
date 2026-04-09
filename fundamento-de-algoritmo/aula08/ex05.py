l = []
quant = int(input("digite a quantidade de numeros..: "))
x = 0
while x < quant:
    num = int(input("Digite um número.: "))
    l.append(num)
    x += 1
print(f"números..: {l}")
print("inverso:")
while quant > 0:
    print(l[quant - 1])
    quant -= 1