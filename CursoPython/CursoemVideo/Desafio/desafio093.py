jogador = dict()
gols = list()
total = 0

print('-='*30)
jogador['Nome'] = str(input('Nome do jogador: '))
cont = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))

for c in range(0, cont):
    gol = int(input(f'Quantos gols na partida {c}?'))
    gols.append(gol)
jogador['gols'] = gols

for g in gols:
    total += g
jogador['total'] = total

print('-='*30)
print(jogador)
print('-='*30)

for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)

print(f'O jogador {jogador["Nome"]} jogou {cont} partidas')
for i,v in enumerate(gols):
    print(f'Na partida {i} fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')
