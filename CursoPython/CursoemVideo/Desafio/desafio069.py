maior = homens = m20 = flag = 0
print("-"*30)
print("CADASTRE UMA PESSOA")
print("-"*30)
while flag != 1:
    idade = int(input("Idade: "))
    if idade > 18:
        maior += 1
    sexo = str(input("Sexo [M/F]: ")).lower()
    if sexo == "m":
        homens +=1
    elif sexo == "f" and idade <20:
        m20 +=1
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

print("Temos {} maiores de 18 anos, {} homens e {} mulheres com menos de 20 anos de idade".format(maior,homens,m20))