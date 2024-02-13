n1 = int(input("Digite o numero: "))
n = n1 - 1
fat = 0
while n != 0:
    n1 = n1*n
    n -= 1
print("Fatorial: {}".format(n1))