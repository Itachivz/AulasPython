saque = 0
c50 = 0
c20 = 0
c10 = 0
c1 = 0

saque = int(input('Qual valor deseja sacar: R$'))
while True:
    if saque % 50 == 0:
        c50 += 1
        saque -= 50
    else:
        if saque % 20 == 0:
            c20 += 1
            saque -= 20
        else:
            if saque % 10 == 0:
                c10 += 1
                saque -= 10
            else:
                if saque % 1 == 0:
                    c1 += 1
                    saque -= 1
                else:
                    break
    if saque == 0:
        break
print(f'{"="*60}')
print(f"""Total de {c50} cedulas de R$50
Total de {c20} cedulas de R$20
Total de {c10} cedulas de R$10
Total de {c1} cedulas de R$1""")