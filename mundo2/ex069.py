idade = 0
maior = 0
homens = 0
menor = 0

while True:
    print('     CADASTRE UMA PESSOA     ')
    print(f'{'='*60}')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
    if sexo == "M":
        homens += 1
    if sexo == "F":
        if idade < 20:
            menor += 1
    if idade > 18:
        maior += 1
    print(f'{'='*60}')
    esc = input('Quer continuar [S/N]: ').upper().strip()
    while esc not in 'SN':
        esc = str(input('Quer continuar [S/N]: ')).upper().strip()
    print(f'{'='*60}')
    if esc == "N":
        break
print(f'{'='*10} FIM DO PROGRAMA {'='*10}')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados!')
print(f'E temos {menor} mulheres com menos de 20 anos!')