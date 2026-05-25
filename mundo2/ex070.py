total = 0
preco = 0
menor = float('inf')
prod1 = 0
print(f'{'='*60}')
print(f'{" "*21}LOJA SUPER BARATAO')
print(f'{'='*60}')
while True:
    prod = input('Nome do produto: ').capitalize()
    preco = float(input('Preco: R$'))
    total += preco
    if preco > 1000:
        prod1 += 1
    if preco < menor:
        menor = preco
        menornome = prod
    print(f'{'='*60}')
    cont = input('Quer continuar [S/N]: ').upper().strip()
    print(f'{'='*60}')
    if cont == "N":
        break
print(f'{"="*15} FIM DO PROGRAMA {"="*15}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {prod1} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {menornome} que custo R${menor:.2f}!')