dados = list()
pessoas = list()
pesadas = list()
leves = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    cont += 1
    dados.clear()
    val = str(input('Deseja continuar? [S/N]: '))
    if val == 'n':
        break
    else:
        print('-'*30)
for c, p in enumerate(pessoas):
    if c == 0:
        maior = p[1]
        menor = p[1]
    elif maior <= p[1]:
        maior = p[1]
    elif menor >= p[1]:
        menor = p[1]

for p in pessoas:
    if p[1] == maior:
        pesadas.append(p)
    elif p[1] == menor:
        leves.append(p)

print('-='*30)
print('O numero de pessoas cadastradas foi: {}'.format(cont))

print('O maior peso foi de {}Kg. Peso de '.format(maior), end=' ')
for p in pesadas:
    print('{}...'.format(p[0]), end=' ')

print()

print('O menor peso foi de {}Kg. Peso de '.format(menor), end=' ')
for p in leves:
    print('{}...'.format(p[0]), end=' ')
