lista = []
for x in range(0, 5):
    lista.append(int(input(f"Digite o valor na posição {x}: ")))
print(f"=-"*60)
print(f"Você digitou os valores: {lista}")

for x, y in enumerate(lista):
    if y == max(lista):
        pos1 = x
    if y == min(lista):
        pos2 = x

print(f"O maior valor digitado foi {max(lista)} na posição {pos1}!")
print(f"O menor valor digitado foi {min(lista)} na posição {pos2}!")