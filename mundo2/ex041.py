idade = int(input('Digite a idade do atleta: '))
if idade <= 9:
    print('Ele e da categoria Mirim!')
elif idade <= 14:
    print('Ele e da categoria Infantil!')
elif idade <= 19:
    print('Ele e da categoria Junior!')
elif idade == 20:
    print('Ele e da categoria Senior!')
else:
    print('Ele e da categoria Master!')