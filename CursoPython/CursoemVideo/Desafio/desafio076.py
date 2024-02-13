print('-'*40)
print('LISTAGEM DE PREÇOS')
print('-'*40)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end='')
    else:
        print('R${:>7.2f}'.format(listagem[pos]))
print('-'*40)