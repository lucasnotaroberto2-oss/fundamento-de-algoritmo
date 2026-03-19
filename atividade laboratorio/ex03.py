num = int(input("digie um número: "))
if num % 2 == 0:
    print("o número digitado é PAR")
    if num % 4 == 0:
        print("o número é multiplo de 4")
    else:
        print("o número não é multiplo de 4")
else:
    print("o número digitado é IMPAR")
    if num % 7 == 0:
        print("o número é multiplo de 7")
    else:
        print("o número não é multiplo de 7")