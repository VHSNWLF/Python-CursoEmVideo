Total = flag = cont = menorPreco = cont2= 0
nomeBarato = ""
print("-"*30)
print("LOJA DE PRODUTOS")
print("-"*30)
while flag != 1:
    Nome = str(input("Nome do Produto: "))
    Valor = float(input("Valor do Produto: "))
    cont2 +=1
    if cont2 == 1:
        menorPreco = Valor
        nomeBarato = Nome
    else:
        if Valor < menorPreco:
            menorPreco = Valor
            nomeBarato = Nome
    if Valor > 1000:
        cont += 1
    Total += Valor
    x = str(input("Quer continuar? [S/N]")).lower()
    if x == "n":
        flag = 1
        break
    elif x != "s":
        while x != "s" or x != "n":
            x = str(input("Quer continuar? [S/N]")).lower()
            if x == "s":
                break
            elif x == "n":
                flag = 1
                break
print("O total gasto foi de {}. {} produtos custam mais de R$ 1000,00. E o nome do produto mais barato é {}".format(Total, cont, nomeBarato))