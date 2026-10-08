grupo = []
lista = []
maiorn = []
menorn = []
while True:
    lista.append(input("Nome: "))
    lista.append(int(input("Peso: ")))
    grupo.append(lista[:])
    lista.clear()

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

maior = grupo[0][1]
menor = grupo[0][1]

for x in grupo:
    if x[1] > maior:
        maior = x[1]
    elif x[1] < menor:
        menor = x[1]

for x in grupo:
    if x[1] == maior:
        maiorn.append(x[0])
    elif x[1] == menor:
        menorn.append(x[0])    
print(f"-="*60)
print(f"O maior peso foi de {maior:1f}Kg peso de {maiorn}")
print(f"O menor peso foi de {menor:1f}Kg peso de {menorn}")