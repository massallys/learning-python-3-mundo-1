#calcular a distância da viagem em km

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(distancia))

if distancia < 200:
    distanciaFinal = distancia * 0.50

    print('E o preço da sua passagem será de R${:.1f}.'.format(distanciaFinal))
else:
    distanciaFinal = distancia * 0.45

    print('E o preço da sua passagem será de R${:.1f}.'.format(distanciaFinal))

