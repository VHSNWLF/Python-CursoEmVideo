preco = float(input("Preço do produto: "))
n1 = int(input("Como deseja pagar?\n[1]A Vista em Dinheiro/Cheque\n[2]A Vista no cartão\n[3]2x no Cartão\n[4]3x ou mais no Cartão\n"))
if n1 == 1:
    desconto = preco-(preco*0.10)
    print("10% de desconto. Valor original: {}\nValor Atual: {}".format(preco,desconto))
elif n1 == 2:
    desconto = preco-(preco*0.05)
    print("5% de desconto. Valor original: {}\nValor Atual: {}".format(preco,desconto))
elif n1 == 3:
    print("0% de desconto. Valor original: {}\nValor Atual: {}".format(preco,preco))
elif n1 == 4:
    desconto = preco+(preco*0.2)
    print("20% de juros. Valor original: {}\nValor Atual: {}".format(preco,desconto))
else:
    print("valor invalido")