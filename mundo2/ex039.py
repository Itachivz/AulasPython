idade = int(input('Digite a sua idade: '))
if idade < 18:
    print(f'Voce ainda vai se alistar, e ainda faltam {18 - idade} anos para se alistar!')
elif idade == 18:
    print(f'Voce tem que se alistar esse ano!')
else:
    print(f'Ja passou o tempo de alistamento, passaram {idade - 18} anos do prazo!')