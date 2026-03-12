#programa tabela quadrada

lado = int(input("digite o lado da sua tabela..:"))
for i in range(1,lado + 1):
    for j in range (1, lado + 1):
        if (i > j):
            print("@", end=" ")
        else:
            print("$", end=" ") 
    print()