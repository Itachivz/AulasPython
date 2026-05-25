maior = float('-inf')
menor = float('inf')
for x in range(1,6):
    peso = float(input(f'Digite o peso da pessoa {x} (Kg): '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso e {maior:.1f}kg, o menor peso e {menor:.1f}kg!')