n = 0
x = 0
y= 0
while n != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    x += n
    y += 1
print(f'A soma dos numeros foi {x-999} e foram digitados {y-1} numeros!')