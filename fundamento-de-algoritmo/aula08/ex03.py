l = []
maiorValor = -999999
maiorIndice = 0
for i in range(10):
    nro = float(input("digite um número para lista..: "))
    l.append(nro)
for i in range(len(l)):
    if l[i] > maiorValor:
        maiorValor = l[i]
        maiorIndice = i
print(maiorValor)
print(maiorIndice)
