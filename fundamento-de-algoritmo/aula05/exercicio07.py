x = 0
quantidade = 0
while True:
    n = int(input("digite um número..:"))
    quantidade = quantidade + 1
    if quantidade <= 10:
        x = x + n
        print(f"a somatoria de seus números é..:{x}")
    else:
        print("fim do programa")
        break