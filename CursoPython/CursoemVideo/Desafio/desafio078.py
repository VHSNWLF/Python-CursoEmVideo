valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    elif maior < valores[c]:
        maior = valores[c]
    elif menor > valores[c]:
        menor = valores[c]
print("Valores: {}".format(valores))

for z in range(len(valores)):
    if maior == valores[z]:
        print("O maior valor foi {} na posição {}".format(maior, z+1))
for z in range(len(valores)):
    if menor == valores[z]:
        print('o menor valor foi {} na posição {}'.format(menor, z+1))