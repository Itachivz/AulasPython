valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for x, y in enumerate(valores):
    print(f"Na posição {x} eu encontrei o número {y}!")
print("FIM!")