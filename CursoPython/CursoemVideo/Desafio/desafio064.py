cont = 0
p = 0
soma = 0
n1 = 0
while p != 999:
    n1 = int(input("Digite um numero [999 para SAIR]: "))
    if n1 == 999:
        p = 999
    else:
        soma += n1
        cont += 1
print("Quantidade: {}".format(cont))
print("Soma: {}".format(soma))
