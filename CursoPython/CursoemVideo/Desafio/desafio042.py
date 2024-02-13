r1 = float(input('Digite sua primeira reta: '))
r2 = float(input('Digite sua segunda reta: '))
r3 = float(input('Digite sua terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2+ r1:
    print('Esses segmentos podem formar um triângulo')
    if r1 == r2 and r2 == r3:
        print("Todos os lados são iguais [EQUILATERO]")
    elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 !=r2) or (r2 == r3 and r2 !=r1):
        print("Dois lados sao iguais [ISOSCELES]")
    else:
        print("Todos os lados são diferentes [ESCALENO]")
else:
    print('Esses segmentos não podem formar um triângulo')