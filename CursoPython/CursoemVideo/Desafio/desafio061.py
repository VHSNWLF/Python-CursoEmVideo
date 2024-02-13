n = int(input("Dgite o primeiro termo da PA: "))
n2 = int(input("Digite razão da PA: "))
print("PA Iniciando")
cont = 0
while cont != 10:
    pa = n+n2
    print("{}".format(pa))
    n = pa
    cont+=1