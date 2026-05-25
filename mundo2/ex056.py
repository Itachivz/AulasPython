maior = -1
idadegrupo = 0
mmi = 0

for x in range(1,5):
    nome = input(f'Digite o nome da pessoa {x}: ')
    idade = int(input(f'Digite a idade da pessoa {x}: '))
    sexo = input(f'A pessoa {x} e do sexo Masc ou Fem: ').lower()
    if idade < 0:
        break
    idadegrupo += idade
    if sexo == "masc":
        if idade > maior:
            maior = idade
            hmv = nome
    if sexo == "fem":
        if idade < 20:
            mmi += 1
mediaidade = idadegrupo / 4
print(f'A idade media do grupo e de {mediaidade:.1f} anos!')
print(f'O homem mais velho e o {hmv.capitalize()} com {maior} anos!')
print(f'Temos {mmi} mulheres menores de idade no grupo!')