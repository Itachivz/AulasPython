from random import randint

print('SISTEMA INICIADO')
pc = randint(0, 5)
escolha = int(input('Escolha: '))

if escolha == pc:
    print('Voce ganhou!')
elif escolha > 5:
    print('Apenas entre 0 e 5!')
else:
    print('Voce perdeu!')
print(f'O numero era: {pc}')