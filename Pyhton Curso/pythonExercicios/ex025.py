#verificar se seu nome tem "Silva" nele

nome = str(input('Qual seu nome completo? ')).strip()


print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
