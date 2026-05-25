aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'O aluno {aluno} esta reprovado!')
elif media >= 5 and media < 7:
    print(f'O aluno {aluno} esta de recuperacao!')
else:
    print(f'O aluno {aluno} foi aprovado!')