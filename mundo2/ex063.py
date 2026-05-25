n = int(input('Quantos termos voce deseja mostrar: '))
x = 0
y = 1
print(f'{x} -> {y}', end=' ')
c = 3
while c <= n:
    z = x + y
    print(f' ->  {z}',end=' ')
    x = y
    y = z
    c += 1
print('FIM!')