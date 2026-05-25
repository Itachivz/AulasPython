n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma vale {s},\no produto é {m}\ne a divisão é {d:.3f}. ', end= '')
print(f'Divisão inteira {di}\ne potência {e}.')