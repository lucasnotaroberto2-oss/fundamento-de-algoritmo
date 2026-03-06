preco = float(input("digite o preço do produto: "))
codigo = int(input("digite o codigo do seu produto: "))
if codigo == 1:
    origem = "sul"
elif codigo == 2:
    origem = "norte"
elif codigo == 3:
    origem = "leste"
elif codigo == 4:
    origem = "oeste"
elif codigo == 5 or codigo == 6:
    origem = "nordeste"
elif codigo == 7 and 8 and 9:
    origem = "sudeste"
elif codigo >= 10 and codigo <= 20:
    origem = "centro-oeste"
elif codigo >=25 and codigo <= 30:
    origem = "noroeste"
else:
    origem = "importado"
print(f"preço.......:{preco}")
print(f"origem......:{origem}")