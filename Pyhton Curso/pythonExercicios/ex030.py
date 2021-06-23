#veririfcar se o número digitado é par ou ímpar

import colorama
from colorama import Fore

num = int(input(Fore.LIGHTRED_EX + 'Me diga um número qualquer: '))

resultado = num % 2

if resultado == 0:
    print(Fore.BLUE + 'O número {} é PAR'.format(num))
else:
    print(Fore.BLUE + 'O número {} é ÍMPAR'.format(num))