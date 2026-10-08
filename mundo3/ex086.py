matriz = [[], [], []]

for x in range(0, 9):
    n = int(input(f"Digite um valor: "))
    if x < 3:
        matriz[0].append(n)
    elif 3 <= x < 6:
        matriz[1].append(n)
    else:
        matriz[2].append(n)
print(f"-="*60)
print(f"""[ {matriz[0][0]} ] [ {matriz[0][1]} ] [ {matriz[0][2]} ]
[ {matriz[1][0]} ] [ {matriz[1][1]} ] [ {matriz[1][2]} ]
[ {matriz[2][0]} ] [ {matriz[2][1]} ] [ {matriz[2][2]} ]""")