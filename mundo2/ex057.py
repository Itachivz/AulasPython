s = None
while s != 'M' and "F":
    s = input('Digite o seu sexo [M/F]: ').strip().upper()
    if s != 'M' and 'F':
        print('Tente novamente!')
print('Sexo correto!')