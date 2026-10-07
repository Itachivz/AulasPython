lista = []
lista.append("Rafael")
lista.append(15)
amor = []
amor.append(lista[:])
lista[0] = "Manuela"
lista[1] = 16
amor.append(lista[:])
print(amor)