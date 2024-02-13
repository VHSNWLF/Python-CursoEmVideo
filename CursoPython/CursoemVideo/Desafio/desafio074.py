import random
import math
maior = menor = 0
for c in range (5):
    g = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
for cont in range (5):
    if cont == 0:
        maior = g[cont]
        menor = g[cont]
    elif g[cont] > maior:
        maior = g[cont]
    elif g[cont] < menor:
        menor = g[cont]
print('Os numeros sortedos foram: {}'.format(g))
print('O maior numero foi {}'.format(maior))
print('O menor numero foi {}'.format(menor))