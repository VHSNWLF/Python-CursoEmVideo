def aumentar(n=0, taxa=0, formato=False):
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(n=0, taxa=0,formato=False):
    res =  n-(n * taxa/100)
    return res if formato is False else moeda(res)


def dobro(n=0,formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def metade(n=0,formato=False):
    res = n/2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: {aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-'*30)