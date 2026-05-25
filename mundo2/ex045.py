from random import choice

lista = ["pedra", "papel", "tesoura"]
pc = choice(lista)

player = input('Escolha Pedra, Papel ou Tesoura: ').lower()

print('JO - KEN - PO!')
if player == "tesoura" and pc == "papel" or player == "pedra" and pc == "tesoura" or player == "papel" and pc == "pedra":
    print('Voce ganhou!')
elif player == pc:
    print('Empate!')
else:
    print('Voce Perdeu!')
print(f'O computador escolheu {pc.capitalize()} e voce escolheu {player.capitalize()}!')