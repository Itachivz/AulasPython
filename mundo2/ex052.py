num = int(input('Digite um numero: '))
div = 0
for x in range(1, num+1):
    if num % x == 0:
        div += 1
    if div > 2:
        primo = False
    else:
        primo = True
        
if primo == True:
    print('O numero e primo!')
elif primo == False:
    print('O numero nao e primo')