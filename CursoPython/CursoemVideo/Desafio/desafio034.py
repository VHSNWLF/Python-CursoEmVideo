salario = float(input('Digite seu salário: '))
if salario>1250:
    salario = salario+(salario*0.10)
    print('Parabéns, você recebeu um aumento de 10%, seu novo salário sera de {:.2f}'.format(salario))
else:
    salario = salario + (salario * 0.15)
    print('Parabéns, você recebeu um aumento de 15%, seu novo salário sera de {:.2f}'.format(salario))