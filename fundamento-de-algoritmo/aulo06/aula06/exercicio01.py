qtd = int(input("digite a quantidade de números a serem testados..: "))
i = 1
total_primos = 0
while i <= qtd:
    numero = int(input(f"digite o número {i}..: "))
    if numero > 1:
        divisor = 1
        quantidade_divisores = 0
        while divisor <= numero:
            if numero % divisor == 0:
                quantidade_divisores += 1
            divisor += 1
        if quantidade_divisores == 2:
            total_primos += 1
    i += 1
print(f"voçe digitou {total_primos} números primos de um total de {qtd} números")
        