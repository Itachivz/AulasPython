pt = int(input('Primeiro termo: '))
rz = int(input('Razao: '))
x = 10

while x > 0:
    pt+=rz
    x-=1
    print(pt, end=' -> ')
print('FIM!')