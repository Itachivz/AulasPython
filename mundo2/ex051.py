pt = int(input('Primeiro termo: '))
raz = int(input('Razao: '))
r = pt
for x in range(0, 10):
    r += raz
    print(r, end=' -> ')
print('FIM!')