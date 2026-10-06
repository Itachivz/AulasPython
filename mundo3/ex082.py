lista = []
par = []
impar = []

while True:
    num = int(input("Digite um valor: "))
    lista.append(num)

    while True:
        cont = input("Deseja continuar? [S/N]: ").upper()

        if cont == "S":
            break
        elif cont == "N":
            break
        else:
            print("Digite apenas [S/N]!")
            continue
    if cont == "N":
        break

for x, y in enumerate(lista):
    if y % 2 == 0:
        par.append(y)
    else:
        impar.append(y)

print(f"-="*60)
print(f"""A lista completa é: {lista}
A lista de pares é: {par}
A lista de ímpares é: {impar}""")