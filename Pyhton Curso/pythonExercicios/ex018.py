#calculando seno, cosseno, tangente

import math

ang = float(input('Digite o angulo que você deseja: \n'))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(ang, seno))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ang, cosseno))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}'.format(ang, tangente))
