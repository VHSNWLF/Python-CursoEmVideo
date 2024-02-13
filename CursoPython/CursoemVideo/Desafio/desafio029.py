km = int(input('Digite a velocidade do seu carro em Km: '))
if km>80:
    resto = km-80
    multa = resto*7
    print('Você foi multado em {:.2f}R$'.format(multa))
else:
    print('Parabéns, você não foi multado')