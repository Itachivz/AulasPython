import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
#hip = (co ** 2 + ca ** 2)
#hip = math.sqrt(hip)
hip = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é: {hip:.2f}!')