l = []
for i in range(10):
    num = int(input("Digite um número..:"))
    l.append(num)
print(f"números..: {l}")
indice = 2
while indice < 10:
    if l[indice] > l[indice - 1] + l[indice - 2]:
        print(l[indice])
    indice += 1