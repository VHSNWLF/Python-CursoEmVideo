cont = 0
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-" * 30)
    if n <0:
        break
    while cont <=10:
        print("{} x {} = {}".format(n,cont,n*cont))
        cont += 1
    print("-" * 30)
    cont = 0
print("FIM")
