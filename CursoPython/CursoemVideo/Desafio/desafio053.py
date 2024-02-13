frase = str(input("Digite uma frase qualquer: "))
frase2 = frase.replace(" ","")
frase2.lower()
qtd = len(frase2)
verdade = 0
posicaoFinal = qtd - 1
posicaoInicial = 0
for c in range(posicaoFinal, -1, -1):
    if frase2[c] == frase2[posicaoInicial]:
        verdade = verdade + 1
    if posicaoInicial <= qtd:
        posicaoInicial = posicaoInicial + 1
if verdade == qtd:
    print("a frase é um palíndromo")
else:
    print("a frase não é um palíndromo")