n = 0
while n == 0:
    sexo = str(input("Digite seu Sexo [M/F]")).upper()
    if sexo == "M":
        n += 1
    elif sexo == "F":
        n += 1
    else:
        print("Erro. Tente novamente")
print("fim")