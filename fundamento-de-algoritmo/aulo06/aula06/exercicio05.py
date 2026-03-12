lado = int(input("digite o lado do tabuleiro..:"))
for i in range(1,lado + 1):
    for j in range(1,lado + 1):
        if i % 2 != 0:
            if (i + j) % 2 == 0:
                print("o", end=" ")
            else:
                print("*", end=" ")
        else:
            if (i + j) % 2 == 0:
                print("%", end=" ")
            else:
                print("#", end=" ")
    print()