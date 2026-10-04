num = [2, 5, 9, 1]
num[2] = 3 #Irá trocar o 9 que está na posição 2 (Python não lê 123456 ele começa pelo 0 logo quem está na primeira posição é 0) pelo 3
num.append(7) #Adiciona o número 7 ao final da lista
num.sort(reverse=True) #Organiza os números em ordem descrescente por conta do (reverse=True)
num.insert(2, 6) #Ira inserir o número 6 na posição 2 (Terceiro número)
if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 4.")
# num.pop(2) #Ira retirar o numero 2 que está na posição 2 (Terceiro número)
# num.remove(2) #Irá remover apenas o primeiro número 2 que aparecer na lista.
print(num)
print(f"Essa lista tem {len(num)} elementos.") #O comando "len" vê quantos elementos tem na lista