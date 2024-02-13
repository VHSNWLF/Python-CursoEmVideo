lista = list()
pares = list()
impar = list()
for c in range(0, 7):
    n = int(input("Digite um valor: "))
    if n %2 == 0:
        pares.append(n)
    elif n %2 == 1:
        impar.append(n)
impar.sort()
pares.sort()
lista.append(impar[:])
lista.append(pares[:])
print('Lista com os valores pares: {}'.format(lista[1]))
print('Lista com os valores impares: {}'.format(lista[0]))