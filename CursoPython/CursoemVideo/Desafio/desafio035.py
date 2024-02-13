r1 = float(input('Digite sua primeira reta: '))
r2 = float(input('Digite sua segunda reta: '))
r3 = float(input('Digite sua terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2+ r1:
    print('Esses segmentos podem formar um triângulo')
else:
    print('Esses segmentos não podem formar um triângulo')


