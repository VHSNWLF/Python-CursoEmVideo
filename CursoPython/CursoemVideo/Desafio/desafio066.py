n = s = cont = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        break
    s += n
    cont += 1
print("Quantidade de termos: {}".format(cont))
print("Soma: {}".format(s))