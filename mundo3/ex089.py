aluno = []
alunotot = []
n = 0

while True:
    alunotot.append(input('Nome: '))
    alunotot.append(float(input('Nota 1: ')))
    alunotot.append(float(input('Nota 2: ')))
    aluno.append(alunotot[:])
    n += 1
    alunotot.clear()

    while True:
        cont = input("Deseja continuar [S/N]: ").upper()
        if cont == "S":
            break
        elif cont == "N":
            break
        else:
            print("Digite apenas [S/N]!")
    if cont == "N":
        break

print(f"-="*60)
print(f'''No.  NOME     MÉDIA   
----------------------''')

for x in range(0, n):
    print(f"{x}  {aluno[x][0]}      {(aluno[x][1] + aluno[x][2]) / 2:.2f}")
print(f'-'*50)

while True:
    mostrar = int(input("Mostrar notas de qual aluno? (Número negativo Interrompe): "))
    if mostrar < 0:
        break
    elif mostrar + 1 > len(aluno):
        print("Digite apenas os números (No.) disponíveis!")
        continue
    print(f"Notas de {aluno[mostrar][0]} são {aluno[mostrar][1:]}")