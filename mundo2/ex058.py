from random import randint

acerto = True

print('SISTEMA INICIADO')
pc = randint(0, 10)
while acerto == True:
    escolha = int(input('Escolha um numero entre 0 e 10: '))

    if escolha == pc:
        print(f'Voce ganhou! O numero era {pc}!')
        acerto = False
    elif escolha > pc:
        print('Menos...')
    elif escolha < pc:
        print('Mais...')
    elif escolha > 10:
        print('Apenas entre 0 e 10!')
print('FIM!')