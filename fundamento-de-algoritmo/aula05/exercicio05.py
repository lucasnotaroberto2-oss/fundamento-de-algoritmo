while True:
    x = int(input("digite um número: "))
    if x != 0 and x <= 10:
        print("valor validado")
        break
    else:
        print("valor invalido, tente novamente")