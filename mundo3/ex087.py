matriz = [[], [], []]
par = 0
for x in range(0, 9):
    n = int(input(f"Digite um valor: "))
    if n % 2 == 0:
        par += n
    if x < 3:
        matriz[0].append(n)
    elif 3 <= x < 6:
        matriz[1].append(n)
    else:
        matriz[2].append(n)

tc = matriz[0][2] + matriz[1][2] + matriz[2][2]
maior = max(matriz[1])

print(f"-="*60)
print(f"A soma de todos os valores pares digitados é {par}")
print(f"A soma dos valores da terceira coluna é {tc}")
print(f"O maior valor da segunda linha é {maior}")
print(f"""[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]""")