valores = []
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    val = str(input('Quer continuar? [S/N]')).lower()
    if val == 'n':
        break
a = valores[:]
b = valores[:]
print("Lista original: {}".format(valores))

for c,z in enumerate(a):
    if a[c] %2 == 1:
        a.pop(c)

for c,z in enumerate(b):
    if b[c] %2 == 0:
        b.pop(c)

print("Lista com os v alores pares: {}".format(a))
print("Lista com os valores impares: {}".format(b))