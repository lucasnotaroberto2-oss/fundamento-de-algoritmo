altura = int(input("digite a altura do retangulo"))
largura = int(input("digite a largura do retangulo"))
for i in range(1,altura + 1):
# "i" é responsavel pelas linhas do programa
    for j in range(1,largura + 1):
    # "j" é responsavel pelas colunas, está dentro de i, portanto só roda  quando se houver mais uma linha em i
        if i == 1 or i == altura or j == 1 or j == largura:
            print("*", end="")
        #sempre que estiver nos limeites(bordas) será printado o simbolo "*", caso contrario não ocorre nada
        else:
            print(" ", end="")
    print()
    #o print do final serve como quebra de linha e impede que o comando "end" posicione todos os elementos em uma linha só