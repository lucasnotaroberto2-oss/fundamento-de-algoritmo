#programa tabuleiro de xadrez

lado = int(input("digite o lado do tabuleiro..:"))
for i in range(1,lado + 1):
    #a variavel "lado" está somada com 1 pois o comando "range" limita a variavel a ir até o penultimo número
    for j in range(1,lado + 1):
        if (i + j) % 2 == 0:
            print("o", end=" ")
        else:
            print("*", end=" ")
    print()
