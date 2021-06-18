#dobro, triplo e raiz quadrada

import math

num = int(input('Digite um numero: '))

dobroNum = num * 2
triploNum = num * 3
raizNum = math.sqrt(num)

print('O dobro de {} vale {}.\n'
      'O triplo de {} vale {}.\n'
      'A raiz quadrada de {} é igual a {:.2f}.\n'.format(
    num, dobroNum,
    num, triploNum,
    num, raizNum
    )
)
