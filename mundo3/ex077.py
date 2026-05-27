palavras = ('aprender','programar','linguagem','python','curso')
for p in palavras:
    print(f'\nNa palavra {p.capitalize()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            
# Formula do Prof. Guanabara