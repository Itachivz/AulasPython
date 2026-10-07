lista = []

while True:
    lista.append(int(input("Digite um valor: ")))

    while True:
        cont = input("Quer continuar? [S/N]: ").upper()

        if cont == "S":
            break
        elif cont == "N":
            break
        else:
            print("Digite apenas [S/N]!")
            continue
    if cont == "N":
        break
lista.sort(reverse=True)
print(f"-="*60)
print(f"Você digitou {len(lista)} elementos.")
print(f"Os valores digitados em ordem decrescente são: {lista}")
if 5 not in lista:
    print("O valor 5 não faz parte da lista!")
else:
    print("O valor 5 faz parte da lista!")