n = int(input("Dgite o primeiro termo da PA: "))
n2 = int(input("Digite razão da PA: "))
print("PA Iniciando")
for c in range(0, 10):
    pa = n+n2
    print("{}".format(pa))
    n = pa