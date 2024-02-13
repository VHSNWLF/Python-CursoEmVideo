soma = 0
for c in range (0, 501):
    if c % 3 == 0:
        print(c)
        soma += c
print("soma: {}".format(soma))