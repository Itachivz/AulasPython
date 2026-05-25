num = int(input('Digite um numero: '))
print("""Qual sera a base de convercao?
      1 - Binario
      2 - Octal
      3 - Hexadecimal""")
esco = int(input('Escolha: '))
if esco == 1:
    print(bin(num) [2:])
elif esco == 2:
    print(oct(num) [2:])
elif esco == 3:
    print(hex(num) [2:])
else:
    print('Voce nao escolheu nenhuma opcao entre 1 e 3!')    