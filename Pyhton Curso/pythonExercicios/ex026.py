frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na {} posição.'.format(frase.index('A') + 1))
print('A última letra A aparaceu na posição {}.'.format(frase.rfind('A') + 1))