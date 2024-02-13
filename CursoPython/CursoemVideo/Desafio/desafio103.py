def jogador(nome='desconhecido', gols='0'):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    return (f'O jogador {nome} fez {gols} gols no campeonato.')


# Programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Numero de Gols: '))
print(jogador(n, g))
