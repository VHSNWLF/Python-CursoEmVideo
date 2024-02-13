jogador = dict()
gols = list()
total = c = 0
time = list()

print('-='*30)
#Entrada de dados
while True:
    jogador['Nome'] = str(input('Nome do jogador: '))
    cont = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
    for c in range(0, cont):
        gol = int(input(f'Quantos gols na partida {c}?'))
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['Partidas'] = cont
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    cont = 0
    while True:
        resp = str(input('Deseja continuar? [S/N] ').upper())
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if resp == 'N':
        break
#Fim entrada de dados


for g in gols:
    total += g
jogador['total'] = total

print('-='*30)

for j in time:
    print(f'O jogador {j["Nome"]} jogou {j["Partidas"]} partidas')
print("-="*30)

#Mostrar os dados de cada jogador
for j in time:
    c = 0
    print(f'Jogador: {j["Nome"]}')
    for g in j['gols']:
        print(f'Na {c+1} partida fez {g} gols')
        c += 1
    print("-="*30)
#Fim

