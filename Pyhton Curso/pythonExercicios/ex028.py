#jogo de advinhação

import random
import colorama

from colorama import Fore
from time import sleep

colorama.init()

print(Fore.YELLOW + '-=-' * 20)
print(Fore.BLUE + 'Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(Fore.YELLOW + '-=-' * 20)

num = int(input(Fore.RESET + 'Em que número eu pensei? '))
print('PRONCESSANDO...')
sleep(3)

Numrand = random.randrange(0, 5)

if num == Numrand:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(Numrand, num))
