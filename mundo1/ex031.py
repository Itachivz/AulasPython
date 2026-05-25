km = float(input("Qual a distancia da sua viagem em km: "))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print(f'Sua passagem ira custar: R${preco:.2f}')