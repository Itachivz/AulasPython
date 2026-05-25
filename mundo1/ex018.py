import math
angulo = float(input('Digite um ângulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'Do ângulo {angulo}, seu seno é {seno:.2f}, seu cosseno é {cosseno:.2f} e sua tangente é {tangente:.2f}.')