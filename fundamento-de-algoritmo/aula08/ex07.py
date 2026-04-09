l = []
soma = 0
for i in range(8):
    temp = int(input("digite as ultimas temperaturas..: "))
    soma += temp
    l.append(temp)
media = soma / 8
maior = 9999999
for i in range(len(l)):
    if l[i] < maior:
        maior = l[i]
print(f"menor..: {maior}")
maiorValor = -999999
for i in range(len(l)):
    if l[i] > maiorValor:
        maiorValor = l[i]
print(f"maior..: {maiorValor}")
print(f"média..: {media}")