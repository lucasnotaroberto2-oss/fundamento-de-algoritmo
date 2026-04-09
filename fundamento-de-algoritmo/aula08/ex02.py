l = [11,7,15,4]
maior = 9999999
for i in range(len(l)):
    if l[i] < maior:
        maior = l[i]
print(f"o menor valor é..: {maior}")
