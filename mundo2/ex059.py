from time import sleep

a = True
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))

while a == True:
    print("="*60)
    esc = int(input(f"""Qual operacao deseja realizar?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa
{"="*60}
Escolha: """))
    if esc == 1:
        print("="*60)
        print(f'{v1} + {v2} = {v1 + v2}')
        sleep(2)
    elif esc == 2:
        print("="*60)
        print(f'{v1} x {v2} = {v1*v2}')
        sleep(2)
    elif esc == 3:
        print("="*60)
        print(f'{max(v1, v2)} > {min(v1, v2)}')
        sleep(2)
    elif esc == 4:
        print("="*60)
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
        sleep(2)
    elif esc == 5:
        print("="*60)
        print('Programa finalizado!')
        a = False
    else:
        print("="*60)
        print('Escolha entre 1 e 5!')
        sleep(2)