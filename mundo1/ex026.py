frase = input('Escreva uma frase: ').upper()
print(f'A letra A aparece {frase.count('A')} vezes na sua frase!')
print(f'A letra A aparece a primeira vez na casa {frase.find('A')+1}')
print(f'A letra A aparece a ultima vez na casa {frase.rfind('A')+1}')