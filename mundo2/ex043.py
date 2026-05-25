peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
qdr = alt * alt
imc = peso / qdr
if imc <= 18.5:
    print('Voce esta abaixo do peso!')
elif imc <= 25:
    print('Voce esta no peso ideal!')
elif imc <= 30:
    print('Voce esta com sobrepeso!')
elif imc <= 40:
    print('Voce esta com obesidade!')
elif imc > 40:
    print('Voce esta com obesidade morbida!')
print(f'Seu imc e {imc:.2f}!')