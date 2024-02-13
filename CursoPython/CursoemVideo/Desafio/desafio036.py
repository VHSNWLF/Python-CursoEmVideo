ValorCasa = float(input("Valor da casa: "))
Salario = float(input("Salário: "))
Tempo = int(input("Em quantos anos você quer pagar essa casa: "))
Mensal = ValorCasa/Tempo
Salario2 = Salario*0.3
if Salario2 < Mensal:
    print("Seu pedido foi negado. Valor excedeu 30%")
else:
    print('Sucesso!')

