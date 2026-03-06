quantidade = 0
somatoria = 0
quantidade_homens = 0
quantidade_mulheres = 0
#quantidade de mulheres com salário a baixo de 600 reais
somatoria_salario_homens = 0
while True:
    idade = int(input("digite o valor da sua idade..:"))
    if idade > 0:
        sexo = input("digite seu sexo(M/F).........:")
        salario = float(input("digite seu salário...........:"))
        if sexo == "m":
            quantidade_homens = quantidade_homens + 1
            somatoria_salario_homens = somatoria_salario_homens + salario
        elif sexo == "f" and salario < 600:
            quantidade_mulheres = quantidade_mulheres + 1
        print("-------------x-------------")
        quantidade = quantidade + 1
        somatoria = somatoria + idade
    else:
        media = somatoria / quantidade
        media_homens = somatoria_salario_homens / quantidade_homens
        print(f"a media das idades do grupo é de.........................:{media}")
        print(f"a media salarial dos homens é de.........................:{media_homens}")
        print(f"a quantidade de mulheres com salário abaixo de 600 R$ é..:{quantidade_mulheres}")
        break
