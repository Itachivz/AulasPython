from time import sleep
s = 0
m = 0
h = 0
while True:
    print(f'Horas: {h} | Minutos: {m} | Segundos: {s}')
    sleep(1)
    if s == 59:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    else:
        s += 1