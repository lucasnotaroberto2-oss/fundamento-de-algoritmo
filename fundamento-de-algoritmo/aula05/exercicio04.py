cont = 0
maior = -999999
while cont < 6:
    num = int(input("digite um número...:"))
    if num > maior:
        maior = num
    cont = cont + 1
print(f"o maior número é...:{maior}")