#verificar qual é o primeiro nome e último nome digitado

nome = str(input('Digite seu Nome Completo: '))

primeiro = nome.split()
ultimo = nome.rsplit()

print('Muito prazer em te conhecer!\n')
print('Seu primeiro nome é {}.'.format(primeiro[0]))
print('Seu último nome é {}.'.format(ultimo[len(ultimo)- 1]))
