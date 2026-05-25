r = 0
for x in range(1,7):
    n = int(input(f'Digite o {x} numero: '))
    if n % 2 == 0:
        r = r + n
print(f'O resultado da soma e {r}')