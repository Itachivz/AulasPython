from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print (f'Os numeros sorteados foram: ', end='')
for x in n:
    print(f'{x} ', end='')
print(f'\nO maior valor sorteado foi {max(n)}!')
print(f'O menor valor sorteado foi {min(n)}!')

#Formula do Prof. Gustavo Guanabara