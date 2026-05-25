from datetime import date

y = 0
z = 0
hj = date.today().year
for x in range(0, 7):
    ano = int(input('Que ano voce nasceu: '))
    if hj - ano < 21:
        y += 1
    else:
        z += 1
print(f'{y} pessoas ainda sao menores de idade, e {z} pessoas ja sao maiores de idade!')