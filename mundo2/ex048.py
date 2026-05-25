n = 0
for x in range(1,500+1):
    if x % 2 == 1:
        if x % 3 == 0:
            n += x
print(f'A soma e igual a {n}')