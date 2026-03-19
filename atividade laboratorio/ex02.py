distancia = int(input("digite a distância pecorrida: "))
if distancia <= 200:
    preco_passagem = distancia * 0.5
else:
    preco_passagem = distancia * 0.45
print(f"{preco_passagem:1.2f}")