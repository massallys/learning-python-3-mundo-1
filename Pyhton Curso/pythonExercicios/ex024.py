#verifificar se o nome de cidade que adicionou começa com "SANTO"

cidade = str(input('Em que cidade você nasceu? ')).strip()

print(cidade[:5].upper() == 'SANTO')
