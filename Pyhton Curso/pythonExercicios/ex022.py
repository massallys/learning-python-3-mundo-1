#formatação de nome

nome = str(input('Digite seu nome completo: \n')).strip()

primeiroNome = nome.split()

print('Analisando seu nome...\n')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiroNome[0], len(primeiroNome[0])))
