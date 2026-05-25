n = 0
while True:
    n = int(input('Deseja ver a tabuada de qual valor: '))
    print(f'{'='*60}')
    if n < 0:
        break
    print(f"""{n} x 1 = {n}
{n} x 2 = {n*2}
{n} x 3 = {n*3}
{n} x 4 = {n*4}
{n} x 5 = {n*5}
{n} x 6 = {n*6}
{n} x 7 = {n*7}
{n} x 8 = {n*8}
{n} x 9 = {n*9}
{n} x 10 = {n*10}""")
    print(f'{'='*60}')
print('Fim!')
    