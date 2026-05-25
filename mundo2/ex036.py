vc = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salario: R$'))
anos = int(input('Digite em quantos anos voce deseja pagar: '))
pm = anos * 12
valpar = vc / pm
if valpar > sal * (30 / 100):
    print('Voce nao pode pegar o emprestimo!')
else:
    print('Voce pode pegar o emprestimo!')