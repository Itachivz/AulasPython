n = 0
x = 0
y = 0
maior = float('-inf')
menor = float('inf')
loop = True

while loop == True:
    n = int(input('Digite um numero: '))
    x += n
    y += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c = input('Deseja continuar (s/n): ').lower()
    if c == "n":
        loop = False
print(f'A media entre os numeros foi {x / y:.2f}, o maior numero foi {maior} e o menor foi {menor}!')