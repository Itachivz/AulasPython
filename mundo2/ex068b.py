from random import randint

vc = 0
n = 0
pc = 0

while True:
    print(f'{'='*60}')
    n = int(input('Escolha um numero [1-10]: '))
    ip = input('Impar ou par [I/P]: ').upper()
    print(f'{'='*60}')
    pc = randint(1, 10)
    if ip == "P":
        if (n + pc) % 2 == 0:
            print('Voce ganhou!')
            vc += 1
        else:
            print('Voce perdeu!')
            break
    elif ip == "I":
        if (n + pc) % 2 == 1:
            print('Voce ganhou!')
            vc += 1
        else:
            print('Voce perdeu!')
            break
    print(f'{'='*60}')
    print(f'Voce jogou {n} e o computador jogou {pc}. Total deu {n + pc}!')
print(f'{'='*60}')
print(f'GAME OVER! Voce venceu {vc} vezes!')
print(f'{'='*60}')
