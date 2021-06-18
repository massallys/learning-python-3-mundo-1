numInformado = int(input('Infome um numero: '))

unidade = numInformado // 1 % 10
dezena = numInformado // 10 % 10
centena = numInformado // 100 % 10
milhar = numInformado // 1000 % 10

print('Analisando o numero {}\n'.format(numInformado))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
