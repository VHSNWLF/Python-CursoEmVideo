import random
n = 0
cont = 1
n1 = random.randint(1,10)
while n == 0:
    n2 = int(input('Escolha um número de 1 a 10, se você acertar o numero em que o computador pensou, você vence\nNúmero:'))
    if n1==n2:
        print('Você venceu!. Porem precisou de {} tentativas'.format(cont))
        n += 1
    else:
        print('Você perdeu. Tente novamente >:(')
        cont += 1
print('Número do computador: {}'.format(n1))