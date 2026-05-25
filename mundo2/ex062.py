pt = int(input('Primeiro termo: '))
rz = int(input('Razao: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{pt} ->", end=' ')
        pt += rz
        cont += 1
    mais = int(input('Quantos termos voce quer mostrar a mais: '))
print('FIM!')