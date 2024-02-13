times = ('fulana', 'fulanu', 'fulane', 'fulanz', 'fulano4', 'fulano5', 'fulano6', 'fulano7', 'fulano8', 'fulano9', 'fulano10')
print('-'*30)
print('Lista de Times: {}'.format(times))
print('-'*30)
print('Os 5 primeiros são: {}'.format(times[0:6]))
print('_'*30)
print('Os 4 últimos são {}'.format(times[-4:]))
print('-'*30)
print('Times em ordem alfabética: {}'.format(sorted(times)))
print('-'*30)

for cont in range(len(times)):
    if cont == 4:
        print('O {} está na {} posição'.format(times[cont], cont))