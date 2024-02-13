import random
from time import sleep
numeros = list()
somaTotal = 0

def sorteio(numeros2):
    print('Sorteando 5 valores da lista: ', end=' ')
    for c in range (0, 5):
        numeros2.append(random.randint(0, 100))
        print(numeros2[c], end=' ')
        sleep(0.3)
    print('PRONTO')
    print(f'A lista original é: {numeros}')


def somaPar(lst, soma):
    for i,v in enumerate(lst):
        if lst[i] %2 == 0:
            soma += v

    print(f'A soma dos numeros pares é: {soma}')


sorteio(numeros)
somaPar(numeros, somaTotal)