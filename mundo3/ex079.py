lista = []

while True:
    x = int(input("Digite um valor: "))
    if x not in lista:
        lista.append(x)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado! Não vou adicionar...") 
    cont = input("Deseja continuar? [S/N]: ").upper()
    if cont == "N":
        break
lista.sort()
print(f"=-"*60)
print(f"Você digitou os valores: {lista}")