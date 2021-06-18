#calculando novo salario

salario = float(input('Qual o salário do funcionário? R$'))

aumento = ((salario / 100) * 15)
result = salario + aumento

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber {:.2f}.'.format(salario, result))
