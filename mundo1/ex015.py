km = float(input('Quantos KM você percorreu com o carro: '))
dias = int(input('Quantos dias você está com o carro: '))
km2 = km * 0.15
dias2 = dias * 60
final = dias2 + km2
print(f'Você terá que pagar: R${final:.2f}!')