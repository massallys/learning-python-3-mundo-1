#calculando hipotenusa

import math

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))

hi = math.hypot(co, ca)

print('A hipotenusa vai medir {:.2f} '.format(hi))