ano = int(input('Digite o ano: '))
u = ano // 1 % 10
d = ano // 10 % 10
if [u, d] == [0, 0]:
    if ano % 400 == 0:
        print(f'O ano {ano} e um ano bissexto!')
    else:
        print(f'O ano {ano} nao e um ano bissexto!')
else:
    if ano % 4 == 0:
        print(f'O ano {ano} e um ano bissexto!')
    else:
        print(f'O ano {ano} nao e um ano bissexto!')
