lista = []
for x in range(0, 5):
    lista.append(int(input(f"Digite o valor na posição {x}: ")))
print(f"=-"*60)
print(f"Você digitou os valores: {lista}")

pos1 = []
pos2 = []
for x, y in enumerate(lista):
    if y == max(lista):
        pos1.append(x)
    if y == min(lista):
        pos2.append(x)

print(f"O maior valor digitado foi {max(lista)} nas posições {pos1}!")
print(f"O menor valor digitado foi {min(lista)} nas posições {pos2}!")