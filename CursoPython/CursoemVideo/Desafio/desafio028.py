import random
n1 = random.randint(1,5)
n2 = int(input('Escolha um número de 1 a 5, se você acertar o numero em que o computador pensou, você vence\nNúmero:'))
print('Número do computador: {}'.format(n1))
if n1==n2:
    print('Você venceu!!!')
else:
    print('Você perdeu >:(')