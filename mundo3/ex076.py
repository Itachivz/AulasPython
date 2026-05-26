preco = ('Pao', 0.70, 'Leite', 7.50, 'Arroz', 24.90, 'Feijao', 14.90, 'Carne', 31.50, 'Frango', 21.90)
print(f'{'='*40}')
print(f'{"LISTAGEM DE PRECOS":^40}')
print(f'{'='*40}')
for pos in range(0, len(preco)):
    if pos % 2 == 0:
        print(f'{preco[pos]:.<30}', end='')
    else:
        print(f'R${preco[pos]:>7.2f}')
print(f'{'='*40}')