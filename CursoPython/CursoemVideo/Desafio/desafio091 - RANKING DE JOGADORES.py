import random
from time import sleep
from operator import itemgetter
c = 1
jogadores = dict()
jogadores['Jogador1'] = random.randint(1, 6)
jogadores['Jogador2'] = random.randint(1, 6)
jogadores['Jogador3'] = random.randint(1, 6)
jogadores['Jogador4'] = random.randint(1, 6)
print('* Valores Sorteados *')
print('-='*30)
for k,v in jogadores.items():
    print(f'O {k} tirou {v}...')
    sleep(1)
print('-='*30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos Jogadores: ')
print('-='*30)
for k,v in ranking:
    print(f'{c} - {k} tirou {v}')
    sleep(1)
    c += 1