cidade = str(input('Digite o nome da sua cidade: ')).strip().upper().split()
s = 'SANTO' in cidade[0]
if s == True:
    print("Sua cidade comeca com SANTO!")
else:
    print('Sua cidade nao comeca com SANTO!')

# Esse de cima ta certo, porem no video do guanabara ele nao havia ensinado if e else, entao nao tem como colocar uma mensagem especial, apenas retornar true ou false

# cidade = str(input('Digite o nome da sua cidade: ')).strip().upper().split()
# print(cidade[0] == 'SANTO')

# Os dois estao certos :)