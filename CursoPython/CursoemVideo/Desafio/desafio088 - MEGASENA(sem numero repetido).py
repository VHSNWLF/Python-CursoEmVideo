import random
n = int(input('Quantos jogos voce quer que eu sorteie? '))
lista = list()
combo = list()
cont = 0
for c in range(0, n):
    while True:
        y = random.randint(1, 60)
        if y not in combo:
            combo.append(y)
            cont += 1
        if cont >= 6:
            break
    combo.sort()
    lista.append(combo[:])
    combo.clear()
    cont = 0
lista.sort()
print('-='*30)
for c in range(0, n):
    print('Jogo {}: {}'.format(c+1, lista[c]))
print('-='*12, end='')
print(' Boa Sorte ',end='')
print('-='*13)