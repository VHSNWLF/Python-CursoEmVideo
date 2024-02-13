valores = []
num = cont = cont2 = 0
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    cont += 1
    if num == 5:
        cont2 = 1
    val = str(input('Quer continuar? [S/N]')).lower()
    if val == 'n':
        break
valores.sort(reverse=True)
print('Valores: {}'.format(valores))
if cont2 ==1:
    print("O valor 5 faz parte da lista")
else:
    print('O valor 5 não faz parte da lista')
