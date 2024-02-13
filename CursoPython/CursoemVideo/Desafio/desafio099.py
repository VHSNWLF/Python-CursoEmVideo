from time import sleep
def maior(*valores):
    maior = 0
    tam = len(valores)
    print('Analisando os valores passados...')
    for i, num in enumerate(valores):
        if i == 0:
            maior = num
        elif maior < num:
            maior = num
        print(num, end='... ')
        sleep(0.3)
    print()
    print(f'O maior numero dentre {valores} foi {maior}. Tamanho: {tam}')


maior(3, 5, 7, 2, 7, 8, 9, 10, 29, 39, 100, 2984, 392, 33, 9)
