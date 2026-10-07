pessoas = []
dados = []
maior = 0
menor = 0

for x in range(0, 3):
    dados.append(input("Nome: "))
    dados.append(int(input("Idade: ")))
    pessoas.append(dados[:])
    dados.clear()

for y in pessoas:
    if y[1] >= 21:
        print(f"{y[0]} é maior de idade.")
        maior += 1
    else:
        print(f"{y[0]} é menor de idade.")
        menor += 1

print(f"Temos {maior} maiores e {menor} menores de idade.")