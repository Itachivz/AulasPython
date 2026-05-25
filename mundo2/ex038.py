n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
if n1 > n2:
    print(f'{n1} e maior que {n2}!')
elif n1 < n2:
    print(f'{n2} e maior que {n1}!')
else:
    print(f'{n1} e {n2} tem os valores iguais!')