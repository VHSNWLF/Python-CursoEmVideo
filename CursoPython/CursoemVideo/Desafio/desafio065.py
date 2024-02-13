cont = 0
p = 0
soma = 0
n1 = 0
maior = 0
menor = 999
while p != -1:
    n1 = int(input("Digite um numero: "))
    if maior < n1:
        maior = n1
        if menor == 999:
            menor = n1
    elif n1 < menor:
        menor = n1
    soma += n1
    cont += 1
    ver = str(input("Deseja continuar [S/N]: ")).upper()
    if ver == "N":
        p = -1
media = soma/cont
print("Maior: {}".format(maior))
print("Menor: {}".format(menor))
print("Media: {}".format(media))