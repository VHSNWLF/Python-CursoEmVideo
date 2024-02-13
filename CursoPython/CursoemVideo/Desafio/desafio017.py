"""co = float(input('Qual o comprimento do Cateto Oposto: '))
ca = float(input('Qual o comprimento do Cateto Adjacente: '))
h = (co**2 + ca**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))"""

import math
co = float(input('Qual o comprimento do Cateto Oposto: '))
ca = float(input('Qual o comprimento do Cateto Adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))
