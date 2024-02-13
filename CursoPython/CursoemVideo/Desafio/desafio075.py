cont = cont2 = 0
numeros = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')), int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
print('=-'*30)
print('Você digitou os valores: {}'.format(numeros))
for c in range(len(numeros)):
    if numeros[0] == numeros[c]:
        cont += 1
print('O valor {} apareceu {} vezes'.format(numeros[0], cont))
for c1 in range(len(numeros)):
    if numeros[c1] == numeros[1]:
        print('O valor {} apareceu na {} posição'.format(numeros[c1], c1+1))
for c2 in range(len(numeros)):
    if numeros[c2] %2 == 0:
        cont2 += 1
print('Os valores pares digitados foram: {}'.format(cont2))
