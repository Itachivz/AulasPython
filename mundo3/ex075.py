n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))
x = (n1, n2, n3, n4)

print(f'Voce digitou os valores: {x}!')
print(f'O valor 9 apareceu {(n1,n2,n3,n4).count(9)} vezes!')
if 3 in x:
    print(f'O valor 3 apareceu na posicao {x.index(3)+1}!')
else:
    print(f'O valor 3 nao foi digitado!')
print(f'Os valores pares digitados foram: ', end='') # Abaixo foi feito pelo Prof. / Acima foi eu que fiz
for n in n1, n2, n3, n4:
    if n % 2 == 0:
        print(n, end=', ')