l = []
x = 0
soma_pares = 0
soma_ind_par = 0
indice = 0
while x < 10:
    num = int(input("Digite um número..: "))
    if num % 2 == 0:
        soma_pares += num
        soma_ind_par += indice
    indice += 1
    l.append(num)
    x += 1
print(f"Números..: {l}")
print(f"soma elementos pares..: {soma_pares}")
print(f"soma elementos indice par..: {soma_ind_par}")