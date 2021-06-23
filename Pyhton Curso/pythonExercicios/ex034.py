#calcular o aumento de um determinado valor de salário

salario = float(input('Qual é o salário do funcionário? R$'))

salFinal: float = 0
novoSal: float = 0

if salario > 1250:
    salFinal = ((salario / 100) * 10)
    novoSal = salario + salFinal

else:
    salFinal = ((salario / 100) * 15)
    novoSal = salario + salFinal

print('Quem ganhava R${:.2f} passar a ganhar R${:.2f} agora.'.format(salario, novoSal))