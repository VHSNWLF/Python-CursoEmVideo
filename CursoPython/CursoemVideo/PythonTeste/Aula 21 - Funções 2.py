from time import sleep


def contador(inicio, fim, passo):
    """
    Faz uma contagem e mostra na tela
    :param inicio: Inicio da Contagem
    :param fim: Fim da Contagem
    :param passo: Passo da Contagem
    :return: sem retorno
    Função criada por Vitor Henrique vendo o video do CursoemVideo
    """
    if inicio > fim or passo < 0:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim-1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)
    elif passo == 0:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de 1 em 1')
        for c in range(inicio, fim):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)
    elif passo > 0:
        print('-=' * 30)
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=' * 30)


def somar(a, b, c=0):
    """

    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    O terceiro valor (c) não é obrigatório
    """
    s = a + b + c
    print(f'A soma vale {s}')


help(contador)
help(somar)
somar(1, 43)


def teste():
    global n
    n = 9
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')


#Programa principal
n = 2
x = 2
teste()
print(f'No programa principal n vale {n}')
print(f'Na função teste x vale {x}')


def somar2(a, b, c=0):
    """

    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    O terceiro valor (c) não é obrigatório
    """
    s = a + b + c
    return s


r1 = somar2(2, 4, 7)
r2 = somar2(3, 4, 7)
r3 = somar2(4, 4, 7)
print(f'As somas valem {r1}, {r2} e {r3}')
