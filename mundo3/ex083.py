lista = []
resultado = False

expressao = input("Digite uma expressão: ")
for caractere in expressao:
    if caractere == "(":
        lista.append("(")
    elif caractere == ")":
        if "(" not in lista:
            print("Sua expressão está errada!")
            resultado = True
            break
        else:
            lista.pop()
        
if resultado == False:
    if "(" in lista:
        print("Sua expressão está errada!")
    else:
        print("Sua expressão está correta!")
    print(lista)