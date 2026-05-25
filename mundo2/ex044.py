preco = float(input('Digite o preco do produto: R$'))
print("""Qual a forma de pagamento?
      [1] - A vista dinheiro/cheque: 10% de desconto
      [2] - A vista no cartao: 5% de desconto
      [3] - Em ate 2x no cartao: preco normal
      [4] - 3x ou mais no cartao: 20% de juros""")
cond = int(input('Escolha (1-4): '))

if cond == 1:
    desc = preco * (10 / 100)
    prec2 = preco - desc
elif cond == 2:
    desc = preco * (5 / 100)
    prec2 = preco - desc
elif cond == 3:
    prec2 = preco
elif cond == 4:
    desc = preco * (20 / 100)
    parc = preco + desc
    totalparc = int(input('Quantas parcelas: '))
    prec2 = parc / totalparc
else:
    print('Voce nao escolheu nenhuma opcao entre 1 e 4!')
if cond in (1, 2, 3, 4):
    print(f'Voce tera que pagar {prec2}!')

    # nao resolvido!