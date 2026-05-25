# FORMA 1
#numero = input('Digite: ')
#s = '000' + numero
#print(f'Unidade: {s[-1]}')
#print(f'Dezena: {s[-2]}')
#print(f'Centena: {s[-3]}')
#print(f'Milhar: {s[-4]}')
# eu nao fiz, peguei do comentario do video :(

n = int(input('Digite um numero entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
# Forma do Guanabara