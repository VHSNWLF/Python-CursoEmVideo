menores = 0
velho = 0
media = 0
cont = 0
nomedovelho = ""
for c in range(0, 4):
    sexo = str(input("Digite seu sexo: [F] [M]\n"))
    sexo.lower()
    if sexo == "m":
        idade = int(input("Digite sua idade: "))
        if idade > velho:
            nome = str(input("Digite seu nome, homi: "))
            nomedovelho = nome
        else:
            nome = str(input("Digite seu nome: "))
    else:
        idade = int(input("Digite sua idade muié: "))
        if idade < 18:
            menores = menores + 1
            nome = str(input("Digite seu nome: "))
        else:
            nome = str(input("Digite seu nome: "))
    cont += idade
media = cont/4
print("O nome do homem mais velho neste grupo é {}, a média de idades é {}, e a quantidade de mulheres menores de idade é {}".format(nomedovelho,media,menores))