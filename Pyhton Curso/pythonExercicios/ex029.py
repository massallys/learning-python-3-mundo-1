import colorama
from colorama import Fore

velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade < 80:
    print(Fore.LIGHTYELLOW_EX + 'Tenha um bom dia! Dirija com segurança!')
else:
    multa = velocidade - 80
    multaFinal = multa * 7

    print(Fore.RED + 'MULTADO! Você excedeu o limite permetido que é de 80km/h')
    print(Fore.RED + 'Você deve pagar uma multa de' + Fore.LIGHTYELLOW_EX + ' R${:.2f}!'.format(multaFinal))
    print(Fore.LIGHTYELLOW_EX + 'Tenha um bom dia! Dirija com segurança!')