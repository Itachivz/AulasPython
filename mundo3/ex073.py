tabela = ('Palmeiras','Flamengo','Fluminense','Athletico-PR','Bragantino','Bahia','Sao Paulo','Coritiba','Cruzeiro','Botafogo','EC Vitoria','Atletico-MG','Internacional','Gremio','Corinthians','Vasco da Gama','Santos','Mirassol','Remo','Chapecoense')

print(f'Lista de times do brasileirao: {tabela}')
print(f'Os 5 primeiros sao: {tabela[0:5]}')
print(f'Os 4 ultimos sao: {tabela[-4:]}')
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print(f'A chapecoense esta na {tabela.index('Chapecoense')+1} posicao!')