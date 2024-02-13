valores = []
num = 0
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado, não vou adicionar...')
    else:
        print('Valor adicionado com sucesso!')
        valores.append(num)
    val = str(input('Quer continuar? [S/N]')).lower()
    if val == 'n':
        break
print('Lista Original: {}'.format(valores))
valores.sort()
print('Lista Crescente: {}'.format(valores))
