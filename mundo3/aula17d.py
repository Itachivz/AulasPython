#a = [2, 3, 4, 7]
#b = a                #ISSO AQUI FAZ UMA LIGAÇÃO NÃO UMA COPIA, COPIA É O ITEM ABAIXO
#b[2] = 8

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")