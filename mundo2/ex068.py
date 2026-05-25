from random import randint

vc = 0
n = 0
pc = 0
x = 0

while True:
    print(f'{'='*60}')
    n = int(input('Escolha um numero [1-10]: '))
    if n > 10:
        print(f'{'='*60}')
        print('Digite um numero entre 1 e 10!')
        continue
    ip = input('Impar ou par [I/P]: ').upper()
    if ip not in ['I', 'P']:
        print(f'{'='*60}')
        print('Escolha I ou P!')
        continue
    print(f'{'='*60}')
    pc = randint(1, 10)
    if (n + pc) % 2 == 0:
        x = 'Par'
    else:
        x = 'Impar'
    if ip == 'P':
        if x == 'Par':
            print('Voce ganhou!')
            vc += 1
        else:
            print('Voce perdeu!')
            break
    elif ip == 'I':
        if x == 'Par':
            print('Voce perdeu!')
            break
        else:
            print('Voce ganhou!')
            vc += 1
    print(f'{'='*60}')
    print(f'Voce jogou {n} e o computador jogou {pc}. Total de {n + pc} deu {x}!')
print(f'{'='*60}')
print(f'Voce jogou {n} e o computador jogou {pc}. Total de {n + pc} deu {x}!')    
print(f'{'='*60}')
print(f'GAME OVER! Voce venceu {vc} vezes!')
print(f'{'='*60}')