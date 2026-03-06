altura = float(input("digite a altura do cilindro(cm): "))
raio = float(input("digite o raio do seu cilindro(cm): "))
#--------------
p = 3.1415
area_base = p * (raio/100) ** 2
area_lateral = (altura/100) * (2 * p * raio)
area_cilindro = area_base + area_lateral
#--------------
print(f"a area do cilinro é: {area_cilindro:5.2f} ms")
tinta = area_cilindro / 15
litros = tinta * 5
tinta < 1
preco = 50
quantidade = 1
tinta == 1
preco = 50
quantidade = 1
tinta == 2
preco = 48
quantidade = 2
tinta == 3
preco = 46
quantidade = 3
tinta > 3 
preco = tinta * 45
quantidade = tinta
if tinta ==1 or tinta == 2 or tinta == 3 or tinta > 3 or tinta < 1:
    print(f"area a ser pintada:{area_cilindro:5.2f}ms")
    print(f"a quantidade de litros necessarios é:{litros:5.2f}")
    print(f"o preço a pagar é: R${preco:5.2f}")
    print(f"a quantidade de tintas é:{quantidade:5.0f}lata(s)")


