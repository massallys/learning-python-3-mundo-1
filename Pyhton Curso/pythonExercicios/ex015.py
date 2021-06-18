#aluguel de carro por preço/dia e km percorrido

carroDia = 60
kmDia = 0.15

diaAlugado = int(input('Quantos dias alugados? '))
kmRodado = float(input('Quantos Km rodados? '))

resultDia = diaAlugado * carroDia
resultKm = kmRodado * kmDia
result = resultDia + resultKm

print('O total a pagar é de R${:.2f}'.format(result))
