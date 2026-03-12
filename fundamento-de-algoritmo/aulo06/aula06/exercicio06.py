n = int(input("digite um número inteiro e positivo..:"))
digitos = 1
divisão = 10
while n / divisão >= 1:
    divisão *= 10
    digitos += 1
print(digitos)
    