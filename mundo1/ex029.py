velocidade = float(input('Quantos km/h o carro estava: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print (f'Voce esta acima do limite! Voce foi multado em R${multa:.2f}!')
else:
    print('Voce esta andando na velocidade permitida!')
