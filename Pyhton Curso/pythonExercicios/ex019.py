#escolhendo um item randomicamente em uma lista

import random

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))

randLista = [nome1, nome2, nome3, nome4]
escolherRand = random.choice(randLista)

print('\nO aluno escolhido foi {}'.format(escolherRand))