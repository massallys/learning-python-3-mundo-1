#caulculando descontos

preco = float(input('Qual é o preço do produto? R$'))

desconto = ((preco / 100) * 5)
result = preco - desconto

print('O preço que custava R${:.2f}, na promoção com desconto de 5% vai custar {:.2f}.'.format(preco, result))