lista = []
posM = 0
for a in range(0, 5):
    num = int(input("Digite um valor: "))
    tam = len(lista)
    if tam == 0:
        print("Adicionado ao final da lista...")
        lista.append(num)
    else:
        for x, y in enumerate(lista):
            if y > num:
                posM = x
                lista.insert(posM, num)
                print(f"Adicionado na posição {posM} da lista...")
                break
        if num >= lista[-1]:
            lista.append(num)
            print("Adicionado ao final da lista...")
print(f"-="*60)
print(f"Os valores digitados em ordem foram {lista}!")