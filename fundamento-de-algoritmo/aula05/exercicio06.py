x = 0
quantidade = 0
while True:
    n = int(input("digite um valor..: "))
    if n != 0:
        x = x + n
        quantidade = quantidade + 1
        media = x / quantidade
    else:
        print(f"a somatoria dos numeros é..:{x}")
        print(f"a quantidade de números é..:{quantidade}")
        print(f"a media dos números é......:{media}")
        break