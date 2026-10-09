from random import randint
from time import sleep

print(f"-"*60)
print("    JOGO DA MEGA SENA   ")
print(f"-"*60)
lista = []

jogos = int(input("Quantos jogos você deseja criar: "))

for y in range(0, jogos):
    jogo_atual = []

    for x in range(0, 6):
        num = randint(1, 60)
        if num in jogo_atual:
            num = randint(1, 60)
        jogo_atual.append(num)

    lista.append(jogo_atual[:])

print(f"-=-=-=     SORTEANDO {jogos} JOGOS     -=-=-=")

for z in range(0, jogos):
    lista[z].sort()
    sleep(1.50)
    print(f"{z+1}º jogo: {lista[z]}")