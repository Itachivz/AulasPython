from time import sleep
tempo = int(input('Digite o tempo: '))
for x in range(tempo, 0, -1):
    print(x)
    sleep(1)
print('ACABOU!')